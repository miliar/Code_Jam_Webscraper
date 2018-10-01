import numpy as np

def parse(input_file, output_file):
    with open(input_file) as f:
        T = int(f.readline().split()[0])
        out = open(output_file, 'w')
        for i in range(T):
            N, P = map(int, f.readline().split())
            Rs = list(map(int, f.readline().split()))
            rows = []
            for _ in range(N):
                rows.append(list(map(int, f.readline().split())))
            sol = solve(N, P, Rs, rows)
            line = "Case #"+str(i+1)+": "+str(sol)
            print(line)
            out.write(line+'\n')
    return

def get_range(q, R):
    lower = 10*q//(11*R)
    if lower*11*R == 10*q:
        pass
    else:
        lower += 1

    upper = 10*q//(9*R)
    return set(range(lower, upper+1))

def solve(N, P, Rs, rows):
    setm = []
    for i in range(N):
        R = Rs[i]
        row = rows[i]
        sets = []
        for q in sorted(row):
            sett = get_range(q, R)
            if sett:
                sets.append(sett)
        setm.append(sets)
    unions = [set.union(*sets) if sets else set() for sets in setm]
    allowed = set.intersection(*unions)
    for sets in setm:
        for sett in sets:
            sett &= allowed
    # setm = [sett for sett in sets if sett for sets in setm]

    if N == 1:
        return len(setm[0])
    # greedy
    first_row = setm[0]
    kits = 0
    for first_row_sett in first_row[:]:
        kit_success = 0
        for serving in sorted(first_row_sett):
            matched = []
            for sets in setm[1:]:
                for sett in sets:
                    if serving in sett:
                        # found a sett in one row
                        matched.append(sett)
                        break
                else:
                    # didn't find a match in a row
                    matched = []
                    break
                # found a sett in one row
                continue
            else:
                # found a series of sett in all rows
                kits += 1
                for sss, sets in zip(matched, setm[1:]):
                    sets.remove(sss)
                kit_success = 1
            # didn't find a match for a serving
        if kit_success:
            pass
    return kits
            



dir = "./"

input_file = dir+"B-test.in"
output_file = dir+"B-test.txt"

input_file = dir+"B-small-attempt0.in"
output_file = dir+"B-small-attempt0.out"

'''
input_file = dir+"B-large.in"
output_file = dir+"B-large.out"
'''
parse(input_file, output_file)




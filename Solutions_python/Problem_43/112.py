'''
Fugliest code I've ever written in a contest.
Oh well, I was in a hurry.
'''

cases = [_.strip("\n") for _ in open("A-large.in","rt").readlines()[1:]]
cases = [(_,len(_)) for _ in cases]
tcases = []
for case,len in cases:
    tcases.append((case, len, [(len-id-1, letter) for id,letter in enumerate(case)]))

outfile = open("A.out","wt")

def get_base(n, str):
    taken_values = {}
    taken_values[str[0][1]] = 1
    ans = 0
    for pow, char in str:
        if not char in taken_values.keys():
            if not (0 in taken_values.values()):
                taken_values[char] = 0
            else:
                taken_values[char] = max(taken_values.values()) + 1
                if taken_values[char] >= n:
                    return None
        ans += taken_values[char] * (n**pow)
    return ans


for case_num, case in enumerate(tcases):
    base = 2
    min_val = None
    while not min_val:
        min_val = get_base(base, case[2])
        base += 1
    #print min_val, base
    while True:
        new_val = get_base(base, case[2])
        base += 1
        #print base, new_val
        if not new_val:
            continue
        if new_val >= min_val:
            break
        min_val = new_val

    outfile.write("Case #%d: %d\n" % (case_num+1, min_val))
    print case_num + 1, case[0], min_val, base

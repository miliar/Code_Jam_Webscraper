import sys, itertools

def readints(fin):
    return list(map(int, fin.readline().strip().split(' ')))

N = 20

def solve(test):
    for i in range(1,N):
        for part1 in itertools.combinations(test, i):
            part2 = test.difference(part1)
            if sum(part1) < min(part2): continue
            if sum(part2) < min(part1): continue
            for m in range(1, len(part1)+1):
                for n in range(1, len(part2)+1):
                    for set1 in itertools.combinations(part1, m):
                        sum1 = sum(set1)
                        for set2 in itertools.combinations(part2, n):
                            if sum1 == sum(set2):
                                return set1, set2
    return "Impossible"


fnamein = 'C-small-attempt5.in'
fnameout = 'C-small-attempt5.out'

fin = open(fnamein, 'r')
fout = open(fnameout, 'w')

numcase = readints(fin)[0]
cases = [set(readints(fin)[1:]) for _ in range(numcase)]
for i in range(numcase):
    casenum = i + 1
    print casenum
    fout.write("Case #%d:\n" % (casenum))
    answer = solve(cases[i])
    if answer == "Impossible":
        fout.write("Impossible\n")
    else:
        fout.write(" ".join(str(num) for num in answer[0])+'\n')
        fout.write(" ".join(str(num) for num in answer[1])+'\n')

fin.close()
fout.close()


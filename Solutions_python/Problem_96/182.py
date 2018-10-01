from sys import argv
from re import sub

def decompose_score(n):
    scores = [n//3]*3
    if n%3 >= 1:
        scores[0] += 1
    if n%3 == 2:
        scores[1] += 1
    return scores

def read(inputfile):
    g = inputfile.readline()
    return sub('\n','',g)

inp = open(argv[1])
T = int(read(inp))

for t in range(T):
    numbers = list(map(int, read(inp).split()))
    N,S,p = numbers[:3]
    count = 0
    for n in range(N):
        # 0 special case, cannot be forced negative with surprising case
        if numbers[3+n] == 0 and p != 0:
            continue
        scores = decompose_score(numbers[3+n])
        already_has_one_near = False
        for i in scores:
            if i >= p:
                count += 1
                break
            elif i == p-1 and S > 0:
                if already_has_one_near is True:
                    S -= 1
                    count += 1
                    break
                else:
                    already_has_one_near = True

    print("Case #%s:" % (t+1), count)

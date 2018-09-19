import sys

def solve(case):
    A = case[0]
    B = case[1]
    K = case[2]
    hers = {}
    winners = 0
    for x in range(0,K):
        for y in range(0,K):
            hers[x&y] = True

    for x in range(0,A):
        for y in range(0,B):
            try:
                _ = hers[x&y]
                winners += 1
            except: pass

    return winners

def get_input():
    lines = sys.stdin.read().split('\n')[1:-1]
    cases = []
    for line in lines:
        line = line.split(' ')
        cases.append(map(lambda x:int(x), line))
    return cases


i = get_input()
for x in range(0,len(i)):
    print "Case #%d: %d" % (x+1,solve(i[x]))

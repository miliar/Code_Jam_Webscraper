from itertools import *

inf = 100000000

def choose(stall):
    maxLs = -1
    best = -1
    besti = -1
    for i in range(len(stall)):
        if stall[i] == '.':
            Ls = i - 1 - stall[:i].rindex('O')
            Rs = stall[i + 1:].index('O')
            score = min(Ls, Rs) * inf + max(Ls, Rs)
            if score > best:
                best = score
                besti = i
    return best, stall[:besti] + 'O' + stall[besti + 1:]
               
def solve(N, K):
    stall='O' + '.' * N + 'O'
    for i in range(K):
        best, stall = choose(stall)
    return best

for case in range(int(raw_input())):
    N,K = map(int,raw_input().split())
    ans = solve(N, K)
    ans1 = ans / inf
    ans2 = ans % inf
    print "Case #%d: %d %d" % (case+1, ans2, ans1)

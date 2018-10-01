import math


def solve():
    f = open("A-large.in", "r")
    T = int(f.readline())
    out = open("output.out", "w")

    for case in range(T):
        split = f.readline().split()
        S =  split[0]
        slen = len(S)
        K = int(split[1])
        list = [0]*len(S)
        for i in range(len(S)):
            if S[i] == '+':
                list[i] = 1
        curr = 0
        actions = 0

        while curr <= slen - K:
            if list[curr] == 1:
                curr = curr + 1
                continue
            else:
                for x in range(K):
                    list[curr + x] = 1 - list[curr + x]
                curr = curr + 1
                actions = actions + 1
        possible = True
        for x in range(slen):
            if list[x] == 0:
                possible = False

        if possible:
            print('Case #%d: %d' % (case + 1, actions))
            out.write('Case #%d: %d\n' % (case + 1, actions))
        else:
            print('Case #%d: IMPOSSIBLE' % (case + 1))
            out.write('Case #%d: IMPOSSIBLE\n' % (case + 1))


solve()

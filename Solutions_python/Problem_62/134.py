'''
Program to solve Problem A from Codejam 2010 1C
Danver Braganza
'''


T = int(raw_input())

for i in range(T):
    N = int(raw_input())
    window = []
    left = []
    right = []
    for j in range(N):
        l, r = map(int, raw_input().split())
        window.append(tuple((l, r)))
        left.append(l)
        right.append(r)
    left.sort()
    right.sort()
    lmap = dict([(l, ind) for ind, l in enumerate(left)])
    rmap = dict([(r, ind) for ind, r in enumerate(right)])
    count = 0
    for l, r in window:
        count += abs(lmap[l] - rmap[r])
    print "Case #%d: %d" % (i + 1, count / 2)


        
        
          

    



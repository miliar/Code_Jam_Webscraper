''' 
4
3 1 5 15 13 11
3 0 8 23 22 21
2 1 1 8 0
6 2 8 29 20 8 18 18 21

Case #1: 3
Case #2: 2
Case #3: 1
Case #4: 3

'''
from sys import stdin

val = int(stdin.readline())

for i in range(1,val+1):
    items = stdin.readline().split()
    items = map(int, items)
    s = items[1]
    p = items[2]
    scores = items[3:]
    pcount = 0
    pminuscount = 0
    
    for score in scores:
        best = score / 3
        if score % 3 and score > 0:
            best += 1
        
        if best >= p:
            pcount += 1
        elif best == p-1 and best > 0:
            pminuscount += 1
        
    total = pcount + min(s, pminuscount)
    
    print 'Case #%s: %s' % (i, total)
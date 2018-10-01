import sys
sys.setrecursionlimit(10000000)
def happy_flipper(ss, k, start, cnt):
    cur = -1;

    for i in range(start, len(ss)):
        if ss[i] == '-':
            cur = i
            break
        
    if cur == -1:
        return cnt

    if cur > len(ss) - k:
        return -1

    for i in range(k):
        ss[cur+i] = '+' if ss[cur+i] == '-' else '-'

    return happy_flipper(ss, k, cur+1, cnt+1)

t = int(raw_input())
for i in xrange(1, t+1):
    raw =  raw_input().split(" ")
    cakes = list(raw[0])
    k = int(raw[1])

    cnt = happy_flipper(cakes, k, 0, 0)
    if cnt == -1:
        print "Case #{}: {}".format(i, "IMPOSSIBLE")
    else :
        print "Case #{}: {}".format(i, cnt)


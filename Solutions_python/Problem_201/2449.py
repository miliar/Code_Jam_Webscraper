#!/usr/bin/env python

OCCUPIED = 'o'
EMPTY = '.'

def get_distance(si):
    ls, rs = (0, 0)
    for i in range(si-1, 0, -1):
        if stalls[i] == EMPTY:
            #print i
            ls += 1
        else:
            break
    for i in range(si+1, len(stalls)):
        if stalls[i] == EMPTY:
            #print i
            rs += 1
        else:
            break
    return (ls, rs)

def add_person():
    #print "Adding person"
    max_lr, min_lr, si = (0, 0, 0)
    for i in range(len(stalls)):
        if stalls[i] == OCCUPIED:
            continue
        ls, rs = get_distance(i)
        #print "%d: %d %d" % (i, ls, rs)
        if (min(ls, rs) > min_lr) or (min(ls, rs) == min_lr and max(ls, rs) > max_lr):
            max_lr = max(ls, rs)
            min_lr = min(ls, rs)
            si = i

    stalls[si] = OCCUPIED
    return max_lr, min_lr

def solve():
    #print stalls
    if K > (2 * N) / 3:
        return (0, 0)

    max_lr, min_lr = 0, 0
    for i in range(K):
        max_lr, min_lr = add_person()

    return max_lr, min_lr

T = input()
for ti in range(1, T + 1):
    fields = raw_input().split()
    N = int(fields[0])
    K = int(fields[1])

    #print "Solving %d: %d %d" % (ti, N, K)
    stalls = [EMPTY for i in range(N + 2)]
    stalls[0] = OCCUPIED
    stalls[-1] = OCCUPIED

    max_lr, min_lr = solve()
    print "Case #%d: %d %d" % (ti, max_lr, min_lr)

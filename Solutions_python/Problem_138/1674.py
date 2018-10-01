from sys import stdin
rl = stdin.readline
T = int(rl())

def solve():
    return True 

for t in xrange(T):
    N = int(rl())    
    Naomi = map(float, rl().split())
    Naomi.sort()
    Ken = map(float, rl().split())
    Ken.sort()
    y = z = 0
    i = j = 0
    while i != N and j != N:
        if Naomi[i] < Ken[j]:
            i += 1
        else:
            i += 1
            j += 1
            y += 1

    i = j = N - 1
    while i != -1 and j != -1:
        if Naomi[i] > Ken[j]:
            z += 1
            i -= 1
        else:
            i -= 1
            j -= 1

    print 'Case #%d: %d %d' % (t + 1, y, z) 


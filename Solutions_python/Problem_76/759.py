def testbit(i, n):
    return (n >> i) & 1

import sys
t = int(sys.stdin.readline())
for ti in range(t):
    n = int(sys.stdin.readline())
    bag = map(int, sys.stdin.readline().split())

    canSplit = all(len(list(filter(lambda candy: testbit(bit, candy), bag))) % 2 == 0
                   for bit in range(20))
    if not canSplit:
        print 'Case #{0}: NO'.format(ti+1)
        continue

    print 'Case #{0}: {1}'.format(ti+1, sum(bag) - min(bag))


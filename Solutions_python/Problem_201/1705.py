import sys
from multiprocessing import Pool
from itertools import combinations
import heapq

class Pqueue:
    def __init__(self):
        self.h = []

    def __len__(self):
        return len(self.h)

    def push(self, x):
        heapq.heappush(self.h, -1 * x)

    def pop(self):
        return -1 * heapq.heappop(self.h)

def solve((N, K)):
    q = Pqueue()
    q.push(N)
    for i in xrange(K - 1):
        x = q.pop()
        y = x / 2
        if x % 2 == 0:
            z = y - 1
        else:
            z = y
        q.push(y)
        q.push(z)
    x = q.pop()
    if x % 2== 0:
        return "%d %d" % (x / 2, x / 2 - 1)
    else:
        return "%d %d" % (x / 2, x / 2)
    print "Done!"
    sys.stdout.flush()

# def f(x):
#     if x == 1:
#         return 1
#     return f(x / 2) * 2

# x = 66
# for i in xrange(1, x/2):
#     y = f(i)
#     print x, i, solve((x, i)), y

# T = int(raw_input())
# for i in range(T):
#     N, K = map(int, raw_input().split())
#     print 'Case #%d:' % (i + 1), solve((N, K))
T = int(raw_input())
p = Pool(4)
args = []
for i in range(T):
    N, K = map(int, raw_input().split())
    args.append((N, K))
ans = p.map(solve, args)
for i in range(T):
    print 'Case #%d:' % (i + 1), ans[i]

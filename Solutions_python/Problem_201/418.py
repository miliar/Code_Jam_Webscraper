import collections
import sys

def halves(n):
    half = n >> 1
    if n & 1:
        return half, half
    else:
        return half, half - 1

assert halves(5) == (2, 2)
assert halves(4) == (2, 1)

def solve(n, k):
    intervals = collections.defaultdict(lambda: 0)
    intervals[n] += 1
    while True:
        largest = max(intervals.keys())
        count = intervals[largest]
        if k <= count:
            return halves(largest)
        for h in halves(largest):
            intervals[h] += count
        del intervals[largest]
        k -= count

tc_len = int(sys.stdin.readline())
for tc in range(tc_len):
    n, k = tuple(int(x) for x in sys.stdin.readline().split())
    x, y = solve(n, k)
    print('Case #' + str(tc + 1) + ': ' + str(x) + ' ' + str(y))

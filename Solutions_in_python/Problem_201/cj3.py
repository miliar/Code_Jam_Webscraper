import heapq
def stall(total, n):
    start, end, mid = 2, total + 1, (total+3)/2
    q = []
    while n:
        mid = (start + end) / 2
        heapq.heappush(q, (-(mid-start-1), [(start, mid-1)]))
        heapq.heappush(q, (-(end-mid-1), [(mid+1, end)]))
        next_range = max(q[0][1])
        if n != 1:
            start, end = next_range
            q[0][1].remove(next_range)
            if not q[0][1]:
                heapq.heappop(q)
        n -= 1
    return max(mid-start, end-mid), min(mid-start, end-mid)

f = open('output3', 'wr')
N = int(raw_input())
for i in range(1, N+1):
    a, b = stall(*map(int, raw_input().split(' ')))
    print 'Case #%d: %d %d\n' % (i, a, b)
    f.write('Case #%d: %d %d\n' % (i, a, b))

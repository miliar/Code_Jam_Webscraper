import heapq

def load_data():
    D = int(raw_input())
    Q = []
    counts = {}
    for d in map(int, raw_input().split()):
        counts[d] = counts.setdefault(d,0)
        counts[d] += 1
        if counts[d] == 1:
            heapq.heappush( Q, (-d,d) )
    return Q,counts

def pop(Q):
    return heapq.heappop(Q)

def push(Q,counts,x,k):
    counts[x] = counts.setdefault(x,0)
    counts[x] += k
    if counts[x] == k:
        heapq.heappush( Q, (-x,x) )

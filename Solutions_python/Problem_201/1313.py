import heapq

if __name__ == '__main__':
    T = int(input())
    for t in range(1, T + 1):
        N, K = map(int, input().split())
        h = []
        heapq.heappush(h, -N)
        for _ in range(K - 1):
            x = -heapq.heappop(h)
            a, b = x // 2, (x - 1) // 2
            heapq.heappush(h, -a)
            heapq.heappush(h, -b)
        x = -heapq.heappop(h)
        a, b = x // 2, (x - 1) // 2
        print("Case #{x}: {y} {z}".format(x=t, y=max(a, b), z=min(a, b)))
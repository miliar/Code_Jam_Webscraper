from heapq import heappush, heappop

T = int(input())
for i in range(1, T + 1):
  N, K = map(int, input().split(' '))
  pancakes = []
  for j in range(N):
    R, H = map(int, input().split(' '))
    pancakes.append((R, H))
  pancakes.sort()
  N = len(pancakes)
  pq = []
  for k in range(K - 1):
    heappush(pq, 2 * pancakes[k][0] * pancakes[k][1])
  maxSoFar = 0
  for k in range(K - 1, N):
    # Choose pancakes[i]
    R, H = pancakes[k]
    curr = R * R + 2 * R * H
    for j in range(K - 1):
      curr += pq[j]
    if curr > maxSoFar: maxSoFar = curr
    heappush(pq, 2 * R * H)
    heappop(pq)
  print('Case #{}: {}'.format(i, maxSoFar * 3.141592653589793))

file_in = open('C-small-attempt0.in')
file_out = open('C-small-attempt0.out', 'w')
# file_in = open('C.in')
# file_out = open('C.out', 'w')

from collections import deque

T = int(file_in.readline())



for t in range(1, T+1):
  N, Q = map(int, file_in.readline().split())

  E = []
  S = []
  D = []

  for i in range(N):
    e, s = map(int, file_in.readline().split())
    E.append(e)
    S.append(s)

  for i in range(N):
    D.append(list(map(int, file_in.readline().split())))

  # floyd
  for k in range(N):
    for i in range(N):
      for j in range(N):
        if D[i][k] != -1 and D[k][j] != -1:
          if D[i][j] == -1 or D[i][k] + D[k][j] < D[i][j]:
            D[i][j] = D[i][k] + D[k][j]

  ans = []
  for i in range(Q):
    dist = [-1] * N
    inq = [False] * N
    u, v = map(int, file_in.readline().split())
    u -= 1
    v -= 1
    # print(u, v)
    dist[u] = 0
    inq[u] = True
    q = deque([u])
    while len(q) > 0:
      now = q.popleft()
      inq[u] = False
      # print('yo', now, dist[now])
      for j in range(N):
        if D[now][j] != -1:
          if E[now] >= D[now][j]:
            tmp = dist[now] + float(D[now][j]) / float(S[now])
            if dist[j] == -1 or tmp < dist[j]:
              dist[j] = tmp
              if not inq[j]:
                q.append(j)
                inq[j] = True
    ans.append(dist[v])

  file_out.write('Case #' + str(t) + ': ' + ' '.join(map(str, ans)) + '\n')

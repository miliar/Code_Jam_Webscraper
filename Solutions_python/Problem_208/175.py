file_in = open('c1.in', 'r')
file_out = open('c.out', 'w')

T = int(file_in.readline())

for t in range(1, T+1):
  n, q = map(int, file_in.readline().split())
  horses = []
  for i in range(n):
    horses.append(list(map(int, file_in.readline().split())))

  edges = []
  for i in range(n):
    edges.append(list(map(int, file_in.readline().split())))

  for i in range(q):
    u, v, = map(int, file_in.readline().split())

  u = 0
  v = n -1
  cache = {v: 0}
  for start in range(v - 1, -1, -1):
    dist = 0
    min_time = -1
    endurance, speed = horses[start]
    for end in range(start + 1, v+1):
      dist += edges[end-1][end]
      if dist > endurance:
        break
      time = float(dist) / speed + cache[end]
      if min_time == -1 or time < min_time:
        min_time = time
    cache[start] = min_time
  print(cache[0])

  file_out.write("Case #{}: {}\n".format(t, cache[0]))
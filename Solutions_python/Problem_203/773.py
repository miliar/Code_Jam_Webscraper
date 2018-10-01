
def solve(R, C, G):
  done = [[False for _ in range(C)] for _ in range(R)]
  for i in range(R):
    for j in range(C):
      if done[i][j] or G[i][j] == '?':
        continue
      c = G[i][j]

      x = i + 1
      done[i][j] = True
      while x < R and G[x][j] == '?':
        G[x][j] = c
        done[x][j] = True
        x += 1
      xl = i - 1
      while xl >= 0 and G[xl][j] == '?':
        G[xl][j] = c
        done[xl][j] = True
        xl -= 1
      xl += 1

      y = j + 1
      while y < C and all([G[xx][y] == '?' for xx in range(xl, x)]):
        for xx in range(xl, x):
          G[xx][y] = c
          done[xx][y] = True
        y += 1

      y = j - 1
      while y >= 0 and all([G[xx][y] == '?' for xx in range(xl, x)]):
        for xx in range(xl, x):
          G[xx][y] = c
          done[xx][y] = True
        y -= 1
      
  return G

      


        


T = int(input())
for TT in range(T):
  R, C = map(int, input().split())
  G = []
  for _ in range(R):
    G.append(list(input()))
  if TT == 97:
    for row in G:
      print(row)
  G = solve(R, C, G)
  print("Case #{}:".format(TT+1))
  for row in G:
    print(''.join(row))


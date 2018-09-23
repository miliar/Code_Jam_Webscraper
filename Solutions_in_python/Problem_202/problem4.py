from collections import defaultdict


if __name__ == "__main__":
  t = int(input())
  for i in range(1, t + 1):
    changes = set()
    points = 0
    N,M = [int(s) for s in input().split(" ")]
    d = {}
    full_rows = {}
    full_diag = set()
    for j in range(1,M+1):
      c,row,col = [s for s in input().split(" ")]
      row = int(row)
      col = int(col)
      d[(row,col)] = c
      if c in ['x','o']:
        points += 1
        full_rows[row] = col
      if c in ['+','o']:
        points += 1
        full_diag.add(col)

    # Deal with the x's
    free_rows = list(set(range(1,N+1)) - set(full_rows))
    free_cols = list(set(range(1,N+1)) - set([full_rows[r] for r in full_rows]))
    for j in range(len(free_rows)):
      row = free_rows[j]
      col = free_cols[j]
      changes.add((row,col))
      if (row,col) in d:
        d[(row,col)] = 'o'
      else:
        d[(row,col)] = 'x'
      points +=1

    # Deal with the +'s
    # fill the first row
    for col in (set(range(1,N+1)) - full_diag):
      changes.add((1,col))
      if (1,col) in d:
        d[(1,col)] = 'o'
      else:
        d[(1,col)] = '+'
      points += 1
    # fill the second row except for the corners
    for col in range(2,N):
      changes.add((N,col))
      if (N,col) in d:
        d[(N,col)] = 'o'
      else:
        d[(N,col)] = '+'
      points += 1

      
    print("Case #{}: {} {}".format(i, points, len(changes)))
    for key in changes:
      print(d[key]+" "+str(key[0])+" "+str(key[1]))



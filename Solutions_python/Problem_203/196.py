from time import time

inp = open('a.in', 'r+')
out = open('a.out', 'w')

T = int(inp.readline())

for t in range(T):
  s = inp.readline().strip().split(' ')
  R, C = int(s[0]), int(s[1])

  data = []
  for r in range(R):
    l = inp.readline().strip()
    data.append(list(l))

  empty = True
  while empty:
    emptyRow = False
    for r in range(R):
      e = True
      for c in range(C):
        if data[r][c] != '?':
          e = False
      if e:
        emptyRow = True
        break
    if not emptyRow:
      for r in range(R):
        letter = '?'
        for c in range(C):
          if data[r][c] == '?':
            if letter == '?':
              for cahead in range(c+1, C):
                if data[r][cahead] != '?':
                  letter = data[r][cahead]
                  break
            data[r][c] = letter
          else:
            letter = data[r][c]
    else:
      for c in range(C):
        letter = '?'
        for r in range(R):
          if data[r][c] == '?':
            if letter == '?':
              for rahead in range(r+1, R):
                if data[rahead][c] != '?':
                  letter = data[rahead][c]
                  break
            data[r][c] = letter
          else:
            letter = data[r][c]
    empty = False
    for c in range(C):
        for r in range(R):
          if data[r][c] == '?':
            empty = True

  out.write("Case #"+str(t+1)+":\n")
  for d in data:
    out.write(''.join(d)+"\n")

out.close()
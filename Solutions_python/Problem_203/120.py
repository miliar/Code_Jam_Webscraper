def get(row):
  ret = ''
  nb = 0
  last = ''
  last_pos = -1
  for i,c in enumerate(row):
    if c == '?':
      nb += 1
    else:
      ret += c*(nb+1)
      nb = 0
      last = c
      last_pos = i
  ret += last*(len(row)-last_pos-1)
  return ret

T = int(input())

for i in range(1,T+1):
  print('Case #{}:'.format(i))
  R, C = map(int, input().split())
  last_filled_row = -1
  last_row = ''
  for r in range(R):
    row = input().strip()
    if row == '?'*C:
      continue
    else:
      current_row = get(row)
      nb_rows = r - last_filled_row
      for j in range(nb_rows):
        print(current_row)
      last_filled_row = r
      last_row = current_row
  nb_rows = R-1 - last_filled_row
  for j in range(nb_rows):
    print(last_row)


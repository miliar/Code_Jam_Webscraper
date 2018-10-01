import sys

inp = open(sys.argv[1])
out = open(sys.argv[1].replace(".in",".out"), "w")

def possible(case, matrix, m):
  set_map = {}
  column_map = {}
  for i in range(m):
    set_map[i] = set()
    column_map[i] = 0
  for row in matrix:
    highest = max(row)
    count = 0
    for column in row:
      if column != highest:
        set_map[count].add(column)
      else:
        if column > column_map[count]:
          column_map[count] = column
      count += 1
  for key in set_map:
    if len(set_map[key]) > 1 or set_map[key] and set_map[key].pop() <  column_map[key]:
      return "Case #%d: NO\n"%case
  return "Case #%d: YES\n"%case



cases = int(inp.readline().strip())
for i in range(cases):
  dimensions = inp.readline().strip().split(" ")
  n, m = int(dimensions[0]), int(dimensions[1])
  matrix = []
  for j in range(n):
    next_line =  map(int,inp.readline().strip().split(" "))
    matrix.append(next_line)
  out.write(possible(i+1, matrix, m))

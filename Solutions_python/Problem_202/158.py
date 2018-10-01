def calculate_point(grid, n):
  point = 0
  for i in xrange(0, n):
    for j in xrange(0, n):
      if grid[i][j] == 'o':
        point += 2
      elif grid[i][j] == 'x' or grid[i][j] == '+':
        point += 1
  return point

def isViolanteRule(grid, r, c, n):
  return isViolantRowColumnRule(grid, r, c, n) or isViolantDiagonalRule(grid, r, c, n)

def isViolantRowColumnRule(grid, r, c, n):
  inval_row_check = 0
  for i in xrange(0, n):
    if grid[i][c] != '+' and grid[i][c] != '.':
      inval_row_check += 1
  if inval_row_check >= 2:
    print 'inval row %d, %d' % (r, c)
    return True

  inval_column_check = 0
  for j in xrange(0, n):
    if grid[r][j] != '+' and grid[r][j] != '.':
      inval_column_check += 1
  if inval_column_check >= 2:
    print 'inval col %d, %d' % (r, c)
    return True

  return False

def isViolantDiagonalRule(grid, r, c, n):
  dig_sum = r+c
  inval_left_check = 0
  for i in xrange(0, n):
    c_i = dig_sum - i
    if c_i >= n or c_i < 0:
      continue
    if grid[i][c_i] != 'x' and grid[i][c_i] != '.':
      inval_left_check += 1
  if inval_left_check >= 2:
    print 'inval left %d, %d' % (r, c)
    return True

  inval_right_check = 0
  dig_sub = r-c
  for j in xrange(0, n):
    c_j = j - dig_sub
    if c_j < 0 or c_j >= n:
      continue
    if grid[j][c_j] != 'x' and grid[j][c_j] != '.':
      inval_right_check += 1
  if inval_right_check >= 2:
    print 'inval right %d, %d' % (r, c)
    return True
  return False

def addModel(grid, n, model):
  model_list = []
  for i in xrange(0, n):
    for j in xrange(0, n):
      prev_style = grid[i][j]
      if prev_style == model or prev_style == 'o':
        continue
      if ( model == '+' or model == 'x' ) and prev_style != '.':
        continue
      grid[i][j] = model
      if isViolanteRule(grid, i, j, n):
        grid[i][j] = prev_style
      else:
        model_list.append((model, i+1, j+1))
  return model_list


 # raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  # read a list of integers, 2 in this case
  n, m = [int(s) for s in raw_input().split(" ")]
  before_grid = [['.'] * n for _ in xrange(0, n)]
  grid = [['.'] * n for _ in xrange(0, n)]

  for _ in xrange(0, m):
    datas = [s for s in raw_input().split(" ")]
    model = datas[0]
    r = int(datas[1]) - 1
    c = int(datas[2]) - 1
    grid[r][c] = model
    before_grid[r][c] = model

  base_idx = -1
  for c in xrange(0, n):
    if grid[0][c] == 'x':
      grid[0][c] = 'o'
      base_idx = c
    elif grid[0][c] == 'o':
      base_idx = c
    else:
      grid[0][c] = '+'
  if base_idx == -1:
    grid[0][0] = 'o'
    base_idx = 0
  for add_r in xrange(1, n-base_idx):
    grid[base_idx+add_r][add_r+base_idx] = 'x'

  for sub_r in xrange(1, base_idx+1):
    grid[sub_r][base_idx-sub_r] = 'x'

  for c in xrange(1, n-1):
    grid[n-1][c] = '+'

  """
  for c in xrange(1, n-1):
    grid[n-1][c] = '+'
  """
  #addlist1 = addModel(grid, n, '+')
  #addlist1 = addModel(grid, n, 'x')
  #addlist1 = addModel(grid, n, 'o')
  #check = any(isViolanteRule(grid, r, c, n) for r in xrange(0, n) for c in xrange(0, n))
  #print check

  addlist = []
  for r in xrange(0, n):
    for c in xrange(0, n):
      if grid[r][c] != before_grid[r][c]:
        addlist.append((grid[r][c], r+1, c+1))


  print "Case #{}: {} {}".format(i, calculate_point(grid, n), len(addlist) )
  for c in addlist:
    print "{} {} {}".format(c[0], c[1], c[2])
  # check out .format's specification for more formatting options

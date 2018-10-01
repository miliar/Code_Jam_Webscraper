import sys

T = int(sys.stdin.readline().strip())

for t in range(0,T):
  N, M = map(int, sys.stdin.readline().strip().split(" "))
  heights = []
  for n in range(0, N):
    line = map(int, sys.stdin.readline().strip().split(" "))
    heights.append(line)

  def is_minimum(y, x):
    start = heights[y][x]
    # check left and right:
    left = filter(lambda x: x > start, heights[y][:x])
    right = filter(lambda x: x > start, heights[y][x+1:])
    top = filter(lambda y: y[x] > start, heights[:y])
    bottom = filter(lambda y: y[x] > start, heights[y+1:])
    if len(filter(None, [left, right])) and len(filter(None, [top, bottom])):
      return True
    return False

  minima = []
  def run():
    # shouldn't have any local minima or maxima
    for y, line in enumerate(heights):
      for x, num in enumerate(line):
        if is_minimum(y, x):
          minima.append((y,x))
    if minima:
      return "NO"
    return "YES"

  ans = run()

  # heights = [map(str, l) for l in heights]
  # for y,x in minima:
  #   heights[y][x] = 'X'
  # for l in heights:
  #   print ' '.join(l)
  print "Case #%d: %s" % (t + 1, ans)
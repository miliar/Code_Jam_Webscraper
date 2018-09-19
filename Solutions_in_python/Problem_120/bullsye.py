import sys

lines = sys.stdin.readlines()

for case in range(1, int(lines[0]) + 1):
  parameters = lines[case].split()
  r = int(parameters[0])
  t = int(parameters[1])

  needed = 2 * r + 1
  can_draw = 0
  while needed <= t:
    t -= needed
    r += 2
    can_draw += 1
    needed = 2 * r + 1

  print "Case #" + str(case) + ":", can_draw


def is_tiddy(num):
  num = map(int, str(num))
  prev = 0
  flag = True
  for i in num:
    if i < prev:
      flag = False
    prev = i
  return flag

def last_tiddy(num):
  while num > 0:
    if is_tiddy(num):
      return int(num)
    num -=1
  return 0

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  #n, m = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
  #a = raw_input()
  print "Case #{0}: {1}".format(i,last_tiddy(int(raw_input())))
  #print "Case #{}: {} {}".format(i, n + m, n * m)
  # check out .format's specification for more formatting options


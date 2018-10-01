

def flip(string, k, pos):
    for x in xrange(k):
        if (string[x + pos] == '-'):
            string[x + pos] = '+'
        else:
            string[x + pos] = '-'



t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  s, m = raw_input().split(" ")
  string = list(s)
  k = int(m)

  flips = 0
  for index, char in enumerate(string):
      if char == '-':
          if (index + k > len(string)):
              break
          else:
              flip(string, k, index)
              flips +=1
  else:
      print "Case #{}: {}".format(i, flips)
      continue


  print "Case #{}: IMPOSSIBLE".format(i)
  # check out .format's specification for more formatting options

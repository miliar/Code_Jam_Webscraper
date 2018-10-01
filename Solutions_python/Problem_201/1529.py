import math

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = long(input())  # read a line with a single longeger
for i in range(1, t + 1):
  N, K = [long(s) for s in raw_input().split(" ")]
  arrive = 1
  space = [N>>1, (N-1)>>1]
  newspace = []
  pointer = 0
  left = space[0]
  right = space[1]
  while(arrive < K):
    arrive = arrive + 1
    left = space[pointer]>>1
    right = (space[pointer]-1)>>1
    newspace.append(left)
    newspace.append(right)
    pointer = pointer + 1
    if(pointer == len(space)):
      space = newspace
      space.sort(reverse=True)
      newspace = []
      pointer = 0
 
  print("Case #{}: {} {}".format(i, max(left,right), min(left,right)))

  # n, m = [long(s) for s in input().split(" ")]  # read a list of longegers, 2 in this case
  #print("Case #{}: {}".format(i, o))
  # check out .format's specification for more formatting options

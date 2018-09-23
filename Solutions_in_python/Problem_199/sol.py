def reverse(f):
    if f == '+':
        return '-'
    return '+'

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for cur_case in xrange(1, t + 1):
  # n, m = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
  faces, width = raw_input().split(" ")
  faces = list(faces)
  width = int(width)
  # print faces
  # print width
  cnt = 0
  for i in range(0, len(faces) - width + 1):
      if faces[i] == '-':
          cnt += 1
          for j in range(0, width):
              faces[i+j] = reverse(faces[i+j])

  for i in range(0, len(faces)):
      if faces[i] == '-':
         cnt = -1
         break
  ans = cnt if cnt >= 0 else 'IMPOSSIBLE'
  print "Case #{}: {}".format(cur_case, ans)
  # check out .format's specification for more formatting options

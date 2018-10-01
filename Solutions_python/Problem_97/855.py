# recycle.py
import sys

T = int(sys.stdin.readline().strip())

for t in range(T):
  line_array = sys.stdin.readline().strip().split()
  A = int(line_array[0])
  B = int(line_array[1])
  matches = []
  for j in reversed(range(B-A)):
    b = j + A + 1
    b = str(b)*2
    for i in range(len(b)/2):
      if int(b[i:i+(len(b)/2)]) in [x+A for x in range(j)]:
        if str(j+A+1) + ":" + str(int(b[i:i+(len(b)/2)])) in matches:
          continue
        else:
          matches.append(str(j+A+1) + ":" + str(int(b[i:i+(len(b)/2)])))
  print "Case #%d: %d" % (t+1,len(matches))

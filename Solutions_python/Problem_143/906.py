cases = int(raw_input())
for case in range(1,cases+1):
  line = raw_input().split()
  A = int(line[0])
  B = int(line[1])
  K = int(line[2])
  count = 0
  for a in range(A):
    for b in range(B):
      r = a&b
      if r<K:
        count = count + 1
  print "Case #%s: %s" % (case,count)
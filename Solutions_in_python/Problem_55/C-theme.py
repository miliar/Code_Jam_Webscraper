def theme(R, k, N, groups):
  l = len(groups)
  rides = 0
  pos = 0
  for i in range(0, R):
    riders = 0
    start_pos = pos
    while riders < k:
      if groups[pos] <= (k - riders):
        riders += groups[pos]
        pos += 1
        pos %= l
        if pos == start_pos:
          break
      else:
        break
    # print "Riders: %d" % riders
    rides += riders
  return rides

if __name__ == "__main__":
  # f = open("C-test.in")
  f = open("C-small.in")
  # f = open("C-large.in")
  T = int(f.readline().strip())
  for i in range(0, T):
     (R, k, N) = f.readline().strip().split(' ')
     groups = f.readline().strip().split(' ')
     groups = map(int, groups)
     print "Case #%d: %s" % (i + 1, theme(int(R), int(k), int(N), groups))

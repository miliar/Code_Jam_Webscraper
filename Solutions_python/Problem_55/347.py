#! /usr/bin/python

fd = open("input.in")

def solve(R, k, N, g):
  total = sum(g)
  if total <= k:
    return total * R

  g.extend(g) # duplicate list for easier manipulation

  next_step = [0] * N
  for i in xrange(0, N):
    tot = 0
    for j in xrange(i, i + N):
      tmp = tot + g[j]
      if tmp > k:
        break
      tot = tmp

    next_step[i] = (j % N, tot)

  if R > 100:
    next_100_step = [0] * N

    for i in xrange(0, N):
      gain = 0
      cur_pos = i
      for j in xrange(0, 100):
        (cur_pos, gain_run) = next_step[cur_pos]
        gain += gain_run
      next_100_step[i] = (cur_pos, gain)

    gain = 0
    cur_pos = 0
    tmp_R = (R - 100) / 100
    for i in xrange(0, tmp_R):
      (cur_pos, gain_run) = next_100_step[cur_pos]
      gain += gain_run

    for i in xrange(tmp_R * 100, R):
      (cur_pos, gain_run) = next_step[cur_pos]
      gain += gain_run

  else:
    gain = 0
    cur_pos = 0
    for i in xrange(0, R):
      (cur_pos, gain_run) = next_step[cur_pos]
      gain += gain_run

  return gain


num_cases = int(fd.readline())

for i in range(0, num_cases):
  (R, k, N) = [int(item) for item in fd.readline().split(" ")]
  g = [int(item) for item in fd.readline().split(" ")]
  output = solve(R, k, N, g)
  print "Case #%d:" % (i+1), output


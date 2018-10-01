T = input()
for case in xrange(T):
  temp, peeps = raw_input().split()
  max_shyness = int(temp)

  res = 0
  cur_count = 0

  for i in xrange(len(peeps)):
    if i == 0:
      cur_count += int(peeps[i])
    else:
      if int(peeps[i]) > 0:
        if cur_count >= i:
          cur_count += int(peeps[i])
        else:
          res += i - cur_count
          cur_count += int(peeps[i]) + (i - cur_count)

  print "Case #%d: %d" % (case+1, res)
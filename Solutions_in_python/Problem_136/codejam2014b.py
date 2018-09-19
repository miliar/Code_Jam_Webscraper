ntests = int(raw_input())
for test in xrange(1, ntests+1):
  [c, f, x] = map(float, raw_input().split())
  prod = 2.0
  cur_elapsed = 0.0
  total = 0.0
  while True:
    time_no_farm = x / prod
    time_with_farm = c / prod + x / (prod + f)
    if time_no_farm < time_with_farm:
      total = cur_elapsed + time_no_farm
      break
    else:
      cur_elapsed += c / prod
      prod = prod + f

  print "Case #{0}: {1:.7f}".format(test, total)

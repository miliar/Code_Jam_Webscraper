#!/usr/bin/env python
infile = "B-small-attempt2.in"
#infile = "B-test.in"

BASE_COOKIES_PER_SECOND = 2.0

def calc_time(c, f, x):
  seconds_passed = 0
  seconds_remaining = x / (BASE_COOKIES_PER_SECOND)
  num_farms = 0

  if (seconds_remaining <= c):
    return seconds_remaining

  rate = BASE_COOKIES_PER_SECOND + (num_farms * f)
  next_rate = BASE_COOKIES_PER_SECOND + ((num_farms+1) * f)
  buy_point = c / rate
  rem_after_buy = x / next_rate

  while buy_point + rem_after_buy < seconds_remaining:
    num_farms += 1
    seconds_passed += buy_point
    seconds_remaining = rem_after_buy

    rate = BASE_COOKIES_PER_SECOND + (num_farms * f)
    next_rate = BASE_COOKIES_PER_SECOND + ((num_farms+1) * f)
    buy_point = c / rate
    rem_after_buy = x / next_rate

  seconds_passed += seconds_remaining
  return seconds_passed

if __name__ == "__main__":
  f = open(infile, "r")
  num_cases = int(f.readline())

  for n in xrange(1, num_cases+1):
    [n_c, n_f, n_x] = [float(v) for v in f.readline().split()]
    t = calc_time(n_c, n_f, n_x)
    print "Case #%s: %.7f" % (n, t)

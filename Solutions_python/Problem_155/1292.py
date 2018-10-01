
def min_friends_invited(shy_hist):
  acc_persons_clapping = 0
  to_add = 0
  for shyness, n_persons in enumerate(shy_hist):
    if n_persons > 0:
      diff = shyness - acc_persons_clapping
      if diff > 0:
        to_add += diff
        acc_persons_clapping += diff
      acc_persons_clapping += n_persons
  return to_add

def main():
  t = int(raw_input())
  for i in xrange(t):
    smax, shy_hist = raw_input().split()
    smax = int(smax)
    shy_hist = map(int, shy_hist)
    r = min_friends_invited(shy_hist)
    print "Case #%d: %d"%(i+1, r)

main()

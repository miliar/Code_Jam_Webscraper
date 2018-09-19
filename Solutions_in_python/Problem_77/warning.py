def gcd(x,y):
    if y==0:
        return x;
    return gcd(y,x%y);

def Solve(L):
  y = L[0]
  L1 = [abs(x - y) for x in L]
  g = reduce(Gcd, L1)
  if y % g == 0:
    return 0
  else:
    return g - (y % g)

cases = int(raw_input());



for cur_case in xrange(cases):
    nums = map(int,raw_input()[1:].split());
    nums.sort();
    print "Case #%d: %d" % (Solve(nums))

    

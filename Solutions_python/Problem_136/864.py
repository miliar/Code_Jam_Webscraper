

def is_worth_buying(C, F, X, rate):
  time_without_buy = X/rate
  time_with_buy = (C/rate) + (X/(rate+F)) 
 
  if time_with_buy < time_without_buy:
    return True
  return False

def calc_min_cookie_time(C,F,X):
  total_time = 0
  rate = 2.0

  farms = 0
  while is_worth_buying(C, F, X, rate):
    total_time += (C/rate)
    rate += F
    farms += 1
    
  # actual time to get the cookies
  total_time += (X/rate)

  return total_time 
  	  

if __name__ == '__main__':
  T = int(raw_input())
  for i in xrange(1,T+1):
    C,F,X = tuple(float(x) for x in raw_input().split())

    min_time = calc_min_cookie_time(C,F,X)

    print "Case #%s: %s" % (i, min_time) 

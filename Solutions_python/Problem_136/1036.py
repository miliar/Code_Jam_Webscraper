import sys

f = open(sys.argv[1], "r")

cases = f.readline()

for case in range(int(cases)):
  row = f.readline()
  ns = list(row.strip().split())
  C = float(ns[0])
  F = float(ns[1])
  X = float(ns[2])

  #print "C:", C ,"F:", F ,"X:", X

  rate = 2
  total_cookies = 0.0
  time = 0.0
  now_total_time = 0.0
  last_time = 0.0
  count = 0
  done = False
  #Equation: Answer = time + (C/rate)

  while(total_cookies < X):

    #Have enough cookies in the farm loop
    if(done):
      break

    total_cookies = total_cookies + rate
    last_time = X/rate + time
    while (total_cookies >= C):
      last_time = X/rate + time

      complete_time_at_rate = (C*1.0)/rate
      time = time + complete_time_at_rate


      total_cookies = total_cookies - C
      rate = rate + F

      now_total_time = X/rate + time

      if (now_total_time > last_time):
        done = True
        break


  print "Case #"+str(case+1)+": %.7f" %round(last_time,7)

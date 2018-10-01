import sys

def CookieClicker(filename):
  f = open(filename)
  case_amount= int(f.readline())
  for i in range(case_amount):
    process_case(i, f)

	
def process_case(i, f):
  line = f.readline()
  parts = line.split()
  C = float(parts[0])
  F = float(parts[1])
  T = float(parts[2])
  print "Case #%d: %f" % (i+1, cc(C,F,T))
 

def cc(C,F,T):
  factory_time=0.0
  current_productivity=2.0
  cookie_time=T/current_productivity  
  total_time = factory_time+cookie_time
  pre_total_time = total_time
  while total_time <=pre_total_time:
    factory_time+=(C/current_productivity)
    current_productivity+=F
    cookie_time=T/current_productivity
    pre_total_time=total_time
    total_time=factory_time+cookie_time
  return pre_total_time
  
if __name__ == "__main__":
  CookieClicker("input.txt")
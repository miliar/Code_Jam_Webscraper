def solve(d,h):
  max_speed = -1.0
  max_time = -1.0
  for hh in h:
    if(hh[0]<=d):
      if((float(d-hh[0])/hh[1]) >  max_time):
        max_time = (float(d-hh[0])/hh[1])
  return float(d)/max_time

t = int(input())  #read a line with a single integer
for i in range(1, t + 1):
  #read a list of integers, 2 in this case
  d, n = [int(c) for c in input().split(" ")] 
  h = []
  for j in range(n):
    k, s = [int(cc) for cc in input().split(" ")]
    h.append((k,s))    
  print("Case #{:0.0f}: {:0.6f}".format(i, solve(d,h)))
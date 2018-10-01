# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

def round_up(x):
  if x == int(x):
    return int(x)
  else:
    return int(x + 1)

def cruise_control(D, N, k_s_pairs):
  last_arrival_time = 0
  for (k, s) in k_s_pairs:
    arrival_time = (D - k) / float(s)
    if arrival_time > last_arrival_time:
      last_arrival_time = arrival_time
  return D / last_arrival_time

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  D, N = [int(s) for s in raw_input().split(" ")]
  k_s_pairs = []
  for j in xrange(N):
    K, S = [int(s) for s in raw_input().split(" ")] 
    k_s_pairs.append((K, S))

  print "Case #{}: {}".format(i, cruise_control(D, N, k_s_pairs))

 # check out .format's specification for more formatting options
num_tests = int(raw_input())

for test in range(num_tests):
  dest,other_horses = map(int,raw_input().split())
  speeds = []
  distances = []
  times = []
  max_time = 0.00;
  slow_index = -1;
  for h in range(other_horses):
    d,s = map(int,raw_input().split())
    rd = dest-d
    distances.append(rd)
    speeds.append(s)
    temp_t = float(rd)/s
    times.append(temp_t)
    if temp_t>max_time:
      max_time = temp_t
      slow_index = h
  print "Case #"+str(test+1)+": "+str(float(dest)/times[slow_index])
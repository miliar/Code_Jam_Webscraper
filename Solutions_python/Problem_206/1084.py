def get_cruise_speed(dest, horses):
  slow_t = -1
  
  for p, s in horses.items():
    d = dest - p
    time = (d * 1.0) / s
    if slow_t < 0 or time > slow_t:
      slow_t = time

  return (dest * 1.0) / slow_t


#main program
test_cases = int(raw_input())

for i in range(test_cases):
  r_c = raw_input().split()
  dest = int(r_c[0])
  horse_c = int(r_c[1])
  horses = {}

  for r in range(horse_c):
    test = raw_input()
    horse_info = test.split()
    horses[int(horse_info[0])] = int(horse_info[1])
  
  c_speed = get_cruise_speed(dest, horses)
  
  print "Case #{0}: {1}".format(i + 1, round(c_speed, 6))
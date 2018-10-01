TYPE = "small"

in_file = open("..\\input\\2012-1C-B-%s.txt" % TYPE, "r")
out_file = open("..\\output\\2012-1C-B-%s.txt" % TYPE, "w")

num_cases = int(in_file.readline().strip())

for case in range(num_cases):     
  out_file.write("Case #%s:\n" % (case + 1))
  other_car = []
  
  values = in_file.readline().strip().split(" ")
  D = float(values[0])
  N = int(values[1])
  A = int(values[2])
  
  for ii in range(N):
    other_car.append([float(x) for x in in_file.readline().strip().split(" ")])
  
  accs = [float(x) for x in in_file.readline().strip().split(" ")]
    
  if N > 1:
    other_car_speed = (other_car[1][1] - other_car[0][1]) / (other_car[1][0] - other_car[0][0])
    other_car_end_time = (D - other_car[0][1]) / other_car_speed
  else:
    other_car_end_time = -1
  
  for acc in accs:
    t_min = (2 * D / acc) ** 0.5
    
    if (t_min < other_car_end_time and other_car_end_time > 0):
      t = other_car_end_time
    else:  
      t = t_min
      
    out_file.write("%.6f\n" % t)
    
in_file.close()
out_file.close()

print "Done!"
#! usr/bin/python

file_read = open("B-large.in", "r")
file_write = open("B-large-output.out", "w")
num = int(file_read.readline()) #number of cases
for i in range(num):
  line = file_read.readline().split()
  #line[0] = farm cost, line[1] = farm rate, line[2] = end goal
  rate = 2
  cookies = float(line[2]) #total number and subtract from here
  farm = float(line[0]) #number needed for farm
  farm_rate = float(line[1]) #farm rate
  seconds = 0
  while True:
    # if 2 cookies per second < (2 + farm cookies per second) - (cookies for farm)
    if cookies / rate < cookies / (rate + farm_rate) + farm / rate:
      seconds += cookies / rate #seconds = total divided by rate
      file_write.write("Case #{0}: {1}\n".format(i + 1, seconds))
      break
    else:
      seconds += farm / rate #seconds = cookies for farm / rate
      rate += farm_rate #rate = rate + farm rate

file_read.close()
file_write.close()

def abs(x):
  if x >= 0:
    return x
  else:
    return -x


f = open("large.in", "r")
f2 = open("large.out", "w")


lines = f.readlines()
cases = int(lines[0])

for case in range(0, cases):
  line = lines[case + 1]
  items = line.split(" ")
  cnt = int(items[0])
  items = items[1:]
  
  # decode stuff
  temp = []
  for i in range(0, cnt):
     temp.append((items[i*2], int(items[i*2+1])))

  # futures
  future_o = [0 for i in range(0, cnt + 1)]
  future_b = [0 for i in range(0, cnt + 1)]

  for j in range(cnt - 1, -1, -1):
    if temp[j][0] == 'B':
      future_b[j] = temp[j][1]
      future_o[j] = future_o[j+1]
    else:
      future_o[j] = temp[j][1]
      future_b[j] = future_b[j+1]

  # emulating
  pos_o = 1
  pos_b = 1
  steps = 0

  for i in range(0, cnt):
    if temp[i][0] == 'O':
      more = abs(pos_o - temp[i][1]) + 1
      pos_o = temp[i][1]
      steps += more
      
      # approach other robot
      if pos_b < future_b[i]:
        pos_b = min(pos_b + more, future_b[i])
      else:
        pos_b = max(pos_b - more, future_b[i])
    elif temp[i][0] == 'B':
      more = abs(pos_b - temp[i][1]) + 1
      pos_b = temp[i][1]
      steps += more

      # approach other robot
      if pos_o < future_o[i]:
        pos_o = min(pos_o + more, future_o[i])
      else:
        pos_o = max(pos_o - more, future_o[i])

    # print i, steps
    # print "O is at", pos_o, "; B is at ", pos_b 
  f2.write("Case #%d: %d\n" % ((case + 1), steps))

f.close()
f2.close()

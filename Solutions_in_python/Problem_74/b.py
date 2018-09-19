f = open('2.in')
out = open('2.out', 'w')

count = int(f.readline())

for num in range(count):
  oPos = 1
  bPos = 1
  oT = 0
  bT = 0

  thisline = f.readline().split()

  numPresses = int (thisline[0])

  for press in range(numPresses):
    person = thisline[2*press + 1]    
    distance = int(thisline[2*press + 2])

    if person == "O":
      newTime = max(bT + 1, oT + abs(oPos - distance) + 1)
      oT = newTime
      oPos = distance
    elif person == "B":
      newTime = max(oT + 1, bT + abs(bPos - distance) + 1)
      bT = newTime
      bPos = distance

  out.write('Case #' + str(1+num) + ": " + str(max(oT, bT)) + '\n')

f.close()
out.close()

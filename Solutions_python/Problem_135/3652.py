f = open('A-small-attempt0.in','r');

lines = f.read().split('\n')
lines = lines[:len(lines)-1]

numcases = int(lines[0])

for x in range(0, numcases):
  row1 = int(lines[x * 10 + 1])
  row2 = int(lines[x * 10 + 6])
  numrow1 = lines[x * 10 + 1 + row1].split()
  numrow2 = lines[x * 10 + 6 + row2].split()

  count = 0
  num = ""

  for i in numrow1:
    if i in numrow2:
      count = count + 1
      num = i

  if count == 0:
    print "Case #" + str(x + 1) + ": Volunteer cheated!"
  elif count > 1:
    print "Case #" + str(x + 1) + ": Bad magician!"
  else: 
    print "Case #" + str(x + 1) + ": " + num

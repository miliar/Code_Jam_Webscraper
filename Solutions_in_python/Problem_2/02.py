class Event:
  def __init__(self, time, action, station):
    self.t = time
    self.a = action
    self.s = station
    
  def __cmp__(self, other):
    if self.t == other.t:
      if self.a == "add" and other.a == "del":
        return -1
      if self.a == "del" and other.a == "add":
        return 1
      return 0
    return cmp(self.t, other.t)
    
  def __str__(self):
    return str(self.t)+", "+self.a+", "+self.s

def countTrain(T, tableA, tableB):
  events = []
  for row in tableA:
    col = row.split(" ")
    events.append(Event(getMinute(col[0]), "del", "a"))
    events.append(Event(getMinute(col[1]) + T, "add", "b"))
  for row in tableB:
    col = row.split(" ")
    events.append(Event(getMinute(col[0]), "del", "b"))
    events.append(Event(getMinute(col[1]) + T, "add", "a"))
  events.sort()
  
  resultA = 0
  resultB = 0
  currentA = 0
  currentB = 0
  for e in events:
    if e.a == "add":
      if e.s == "a":
        currentA += 1
      else:
        currentB += 1
    else:
      if e.s == "a":
        if currentA == 0:
          resultA += 1
        else:
          currentA -= 1
      else:
        if currentB == 0:
          resultB += 1
        else:
          currentB -= 1
  return str(resultA) + " " + str(resultB)

def getMinute(hhmm):
  hhmm = hhmm.split(":")
  h = int(hhmm[0]) * 60
  m = int(hhmm[1])
  return h + m

fin = open("input.txt", "r")
fout = open("output.txt", "w")
case = int(fin.readline())
for i in range(case):
  T = int(fin.readline())
  line = fin.readline().split(" ")
  NA = int(line[0])
  NB = int(line[1])
  tableA = []
  tableB = []
  for j in range(NA):
    tableA.append(fin.readline()[:-1])
  for j in range(NB):
    tableB.append(fin.readline()[:-1])
  fout.write("Case #%d: %s\n" % (i+1, countTrain(T, tableA, tableB)))

fin.close()
fout.close()

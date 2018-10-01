fout = open('./out.txt', 'w+')
with open('in.txt') as f:
  T = int(f.readline())
  for i in range(T):
    f.readline()
    naomi = map(float, f.readline().split(' '))
    ken = map(float, f.readline().split(' '))

    naomi.sort()
    ken.sort()
    #print naomi
    #print ken

    naomiCopy = list(naomi)
    kenCopy = list(ken)
    deceitful_max = 0
    while len(naomiCopy) > 0:
      #print "comparing " + str(naomiCopy[0]) + " and " + str(kenCopy[0])
      if naomiCopy[0] < kenCopy[0]:
        del naomiCopy[0]
        del kenCopy[-1]
      else:
        del naomiCopy[0]
        del kenCopy[0]
        deceitful_max += 1
    #print "deceitful max: " + str(deceitful_max)

    naomiCopy = list(naomi)
    kenCopy = list(ken)
    normal_max = 0
    while len(naomiCopy) > 0:
      kenCanWin = False
      cur = 0
      while cur < len(kenCopy):
        if kenCopy[cur] > naomiCopy[0]:
          del kenCopy[cur]
          del naomiCopy[0]
          kenCanWin = True
          break
        cur += 1
      if kenCanWin == False:
        del kenCopy[0]
        del naomiCopy[0]
        normal_max += 1

    #print "normal max: " + str(normal_max)
    fout.write("Case #" + str(i+1) + ": " + str(deceitful_max) + " " + str(normal_max) + "\n")
    print "Case #" + str(i+1) + ": " + str(deceitful_max) + " " + str(normal_max)

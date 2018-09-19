import sys
from itertools import *    

ip,op = sys.argv[1:3]

ipf = open (ip,'r')

tc = int(ipf.readline().strip())
cno=1
opf = open(op,'w')
c = 2**(-40)
while cno<=tc:
    ln = ipf.readline().split()
    n = int(ln[0])
    x = [ int(temp) for temp in ln[1:] ]
    opf.write("Case #%d:\n" % cno)
# from python recipes
    def powerset(iterable):
        s = list(iterable)
        return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
    px = powerset(x)
    sums_seen = [] 
    sets_seen = []
    i = 1
    found = False
    for ss in px:
      tempsum = sum(ss)      
      if tempsum in sums_seen:
        found = True
        currss = ss
        currsum = tempsum
        break
      else:
        sums_seen.append(tempsum)
        sets_seen.append(ss)
      i+=1
    if found:
      for e in currss:
        opf.write("%d " % e)
      opf.write("\n")
      idx = sums_seen.index(currsum)
      for e in sets_seen[idx]:
        opf.write("%d " % e)
      opf.write("\n")
    else:
      opf.write("Impossible\n")
    cno+=1

ipf.close()
opf.close()

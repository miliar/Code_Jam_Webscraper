import sys
import re
import os

def freecell():
  
  N,Pd,Pg = map(int, next(fin).split())
#  print "N K B T", N, K, B, T
  
  possible = 0
  if N > 100:
    if Pd < 100 and Pg == 100:
      print>>fout, "Broken"
      return
    if Pd > 0 and Pg == 0:
      print>>fout, "Broken"
      return
    
    print>>fout, "Possible"
    return
      
  for x in range(1, N + 1):
    if (Pd*x)%100:
      continue
    if Pd < 100 and Pg == 100:
      continue
    if Pd > 0 and Pg == 0:
      continue
    else:
      possible = 1
    
  if possible:
    print>>fout, "Possible"
  else:
    print>>fout, "Broken"                
#  print>>fout, total
    

    
    
if len(sys.argv) != 2:
  print 'specify input file'
  exit()


fin = open(sys.argv[1])
fout = open(os.path.splitext(sys.argv[1])[0]+'.out','w')

numCases = int(next(fin))
for caseNo in range(numCases):
  print>>fout, 'Case #%s:'%(caseNo+1),
  freecell()

fin.close()
fout.close()


  
  


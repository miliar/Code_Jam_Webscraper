
import sys

with open(sys.argv[1],'r') as fin, open(sys.argv[2],'w') as fout:
  numCase = int(fin.readline())
  c = 1
  while c <= numCase:
    smax, ss = fin.readline().split()
    smax = int(smax)
    nums = [int(s) for s in ss] 
    total=0
    shorts = []
    for si, num in enumerate(nums):
      shorts.append(si - total)
      total = total + num
  
    print("Case #%d: %d" %(c, max(shorts)), file=fout)
    
    c = c + 1
  


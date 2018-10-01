##  ###############################
##  ###############################
##  Code Jam 2013 Problem 1
##  chang.liu@jhu.edu
##
##  #############################
##  #############################

from math import sqrt, ceil

fp = open("C-small-attempt0.in", "r")
out = open('C-small-attempt0.out', 'w')
n = int(fp.readline().strip())

for i in range(n):
  nums = fp.readline().split()
  low = int(nums[0])
  high = int(nums[1])
  count = 0
  
  seed = int(ceil(sqrt(low)))
  seed2 = int(seed ** 2)
  
  while(seed2 <= high):
    tmp = str(seed2)
    if tmp == tmp[::-1]:
      tmp = str(seed)
      if tmp == tmp[::-1]:
        count += 1
    
    seed += 1
    seed2 = int(seed ** 2)
    
  out.write('Case #' + str(i+1) + ': ' + str(count) + '\n')
  
fp.close()
out.close()
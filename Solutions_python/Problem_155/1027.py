import os
import re
import string
import sys
import time

start = time.time()

filename = sys.argv[1]
file = open(filename, "rb")

cases = int(file.readline())
for case in range(1, cases+1):
   
   input = file.readline().split()
   max = int(input[0])
   clapping = int(input[1][0])
   friends = 0
   for i in range(1, max+1):
      entry = int(input[1][i])
      if (clapping >= i):
         clapping += entry
      else:
         clapping += (entry + 1)
         friends += 1
         
   print "Case #%d: %d" % (case, friends)
   
file.close()

end = time.time()

sys.stderr.write("%f" % (end-start))

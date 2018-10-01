# Recycled numbers (Question C)
# Google codejam - 14 April 2012

from random import randint

def get_input(filename):
   file = open(filename,'r')
   lines = [line.strip() for line in file.readlines()]
   file.close()
   return lines
   
input_lines = get_input("B:\\Downloads\\C-small-attempt2.in")

def is_recycled_pair(n, m):

   if not (n < m): return False

   n = str(n)
   m = str(m)
   
   if len(n) != len(m): return False
   
   for i in xrange(1,len(n)):
      if (n[-i:] + n[:-i]) == m:
         return True
         
   return False

i = 1
for test_case in input_lines[1:]:
   test_case = test_case.split()
   A = int(test_case[0])
   B = int(test_case[1])
   
   pairs = 0
   for n in xrange(A, B):
      for m in xrange(n+1, B+1):
         if is_recycled_pair(n,m):
            pairs += 1
            if i == 6: print "Pair: (%d, %d)" % (n, m)
            
   print "Case #%d: %d" % (i, pairs)
   i += 1
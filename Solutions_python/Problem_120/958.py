import sys, math
from decimal import *

f = open(sys.argv[1], 'r')
cases = f.readline()
case = 1
for line in f:
  getcontext().prec = 500 
  line = line.rsplit()
  rad = Decimal(int(line[0]))
  ml = Decimal(int(line[1]))

  #print rad, ml
  #n = (1.0/4.0) * (math.sqrt(4*(rad**2) - 4 * rad + 8 * ml + 1 ) - 2 * rad + 1)
  n = (Decimal(1)/Decimal(4)) * (Decimal(Decimal(4)*ExtendedContext.power(rad,Decimal(2)) - Decimal(4) * rad + Decimal(8) * ml + Decimal(1) ).sqrt() - Decimal(2) * rad + Decimal(1))
  n = int(n)

  foo = "Case #" + str(case) + ": "
  sys.stdout.write(foo)
  sys.stdout.write(str(n))
  sys.stdout.write('\n')

  
  case = case + 1

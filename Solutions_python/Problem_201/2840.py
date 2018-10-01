from itertools import *
import math 
import sys
import string
digs = string.digits + string.letters

def int2base(x, base):
  if x < 0: sign = -1
  elif x == 0: return digs[0]
  else: sign = 1
  x *= sign
  digits = []
  while x:
    digits.append(digs[x % base])
    x /= base
  if sign < 0:
    digits.append('-')
  digits.reverse()
  return ''.join(digits)


t = input()
for case in xrange(1,t+1):
	n = input()
	x=2
	while 1==1:
		ans = int2base(n,x)
		
		f=0
		for y in list(str(ans)):
			if y!='1':
				f=1
				break

		if f==0 :
			print "Case #%d: %d"%(case,x)
			break

		x+=1

#!/usr/bin/python
import sys

f = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin

tc=int(f.readline())
for i in range(1,tc+1):
	ln=str(int(f.readline()))
	rep=1	

	while rep:
		rep=0
		for j in range(1,len(ln)):
			if ln[j-1]>ln[j]:
				if j>1:
					ln=ln[:j-1]+chr(ord(ln[j-1])-1)+"9"*(len(ln)-j)
				elif ln[0]>"1":
					ln=chr(ord(ln[j-1])-1)+"9"*(len(ln)-j)
				else:
					ln="9"*(len(ln)-j)
				rep=1
				break
				
		
			
	print("Case #{}: {}".format(i,ln))


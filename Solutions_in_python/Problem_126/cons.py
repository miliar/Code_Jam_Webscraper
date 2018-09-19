#!/usr/bin/python

import sys
import re


def is_cons(c):
	if c!='a' and c!='e' and c!='i' and c!='o' and c!='u':
		return True
		
T = int(sys.stdin.readline())

for i in range(1,T+1):
	res = re.findall('[a-z]+|\d+', sys.stdin.readline())
	W = res[0]
	N = int(res[1])
	firstc = -1
	lastc = -1
	prevfirstc = 0
	count = 0;
	
	#print 'W:'+W+' N:'+str(N)
	for j in range(0,len(W)):
		if is_cons(W[j]):
			firstc = j
			jn = j
			#print 'j:'+str(j)
			while jn<len(W) and is_cons(W[jn]) :#and (jn-j+1)<N: 
				lastc = jn
				if(lastc - firstc +1) == N:
					break
				jn = jn+1
			#print 'jn:'+str(jn)
			if (lastc-firstc+1) == N:
				prevchars = firstc - prevfirstc;
				nextchars = len(W)-1-lastc
				count += 1 + prevchars + nextchars + prevchars * nextchars
				prevfirstc = firstc+1
				#print 'firstc:'+str(firstc)+' lastc:'+str(lastc)+' prevchars:'+str(prevchars)+' nextchars:'+str(nextchars)+' prevfirstc:'+str(prevfirstc)+' count:'+str(count)
	
	print 'Case #'+str(i)+': '+str(count)
				
			
			
				
		

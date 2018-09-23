#!/usr/bin/python
import sys
import array

f = open(sys.argv[1],'r')
t = int(f.readline())

for case in range(t):
	n = [int(x) for x in list(f.readline().strip())]
	y = [str(x) for x in n]
	for i in range(len(n)-1):
		if (n[i]<=n[i+1]):
			y[i] = str(n[i])
			continue
		if(n[i] == 1):
			y[0] = ""
			for j in range(1,len(n)):
				y[j] = "9"
			break
		elif (i>0 and n[i]==n[i-1]):
			for j in range(i):
				if(n[j]<n[i]):
					y[j] = str(n[j])
				else:
					y[j] = str(n[i]-1)
					i = j
					break
			for j in range(i+1,len(n)):
				y[j] = "9"
			break
		else:
			y[i] = str(n[i]-1)
			for j in range(i+1,len(n)):
				y[j] = "9"
			break
	print ("Case #" + str(case+1) + ": " + str("".join(y)), end="\n")
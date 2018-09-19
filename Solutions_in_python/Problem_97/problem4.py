#!/usr/bin/python

import sys

if 1==1:#sys.stdin.readline().rstrip("\n")=='Input':
	count = int(sys.stdin.readline(),10)
	#sys.stdout.write("Output\n")
	for z in range(0,count):
		line=sys.stdin.readline().rstrip("\n")
		in_=line.split()
		b=int(in_[1],10)
		a=int(in_[0],10)
		r=0
		val={}
		for i in range(a,b+1):
			line=str(i)
			for l in range(0,len(line)):
				num=line[l:len(line)]+line[0:l]
				num_n = int(num,10)
	
				if num[0]!='0' and a<=num_n and num_n<i and i<=b:
					if val.has_key(str(i)+str(num)+'n'):
						e=0
					else:
						val[str(i)+str(num)+'n']=1
						r=r+1

		sys.stdout.write("Case #"+str(z+1)+": "+str(r)+"\n")

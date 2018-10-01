import re
import math

f = open("D-small-attempt1.in","r")
w = open("output_d1.txt","w")
num = f.readline()
for i in range(0,int(num)):
	ans = ['GABRIEL','RICHARD']
	res = ''
	x,r,c = [int(l) for l in f.readline().split()]
	allpos = []
	for i1 in range(x,int(math.ceil((x/2.0)))-1,-1):
		d1 = i1
		if x-i1 == 0: allpos.append([d1,1])
		elif x-i1 == 1: allpos.append([d1,2])
		else:
			d2 = 2
			while d2+d1<=x+1:
				allpos.append([d1,d2])
				d2+=1
	allpos = sorted([sorted(d,reverse=True) for d in allpos],reverse=True)
	minedge = min([r,c])
	maxedge = max([r,c])
	# print allpos
	found = False
	for pos in allpos:
		if x == r and x == c : break
		else:
			if minedge*maxedge % pos[0]*pos[1] != 0:
				found = True
	res = ans[0] if not found else ans[1] 
	print("Case #{0}: {1} ".format(i+1,res))
	w.write("Case #{0}: {1}\n".format(i+1,res))
w.close()
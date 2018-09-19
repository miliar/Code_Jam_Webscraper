def imp(start,end,fac,i):
	if (start*fac >= end):
		return i
	else:
		k = fac
		while (start*k*k < end):
			k = k*fac
		return imp(start,start*k,fac,i+1)

myin = open("B.in")
myout = open("B1C.out","w")
inputnum = int(myin.readline().strip())
for k in range(1,inputnum+1):
	info = myin.readline().strip().split()
	start = int(info[0])
	end = int(info[1])
	fac = int(info[2])
	myout.write("Case #")
	myout.write(str(k))
	myout.write(": ")
	myout.write(str(imp(start,end,fac,0)))
	myout.write("\n")
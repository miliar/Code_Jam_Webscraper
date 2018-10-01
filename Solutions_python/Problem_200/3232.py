
fin = open("in")
fout = open("out","w")


def Tide(n):
	n = str(n)
	out = []
	sw = -1
	for i in range(len(n)-1):
		if int(n[i]) > int(n[i+1]):
			sw = i
			break
	if sw ==-1:
		return n
	else:
		print sw
		fp = Tide(int(n[0:sw+1])-1)
		fp = fp if fp !="0" else ""
		sp = "9"*(len(n)-sw-1)
		return fp+sp



t = int(fin.readline())
for case in range(t):
	n = int(fin.readline())	
	fout.write("Case #"+str(case+1)+": "+str(Tide(n))+"\n")

	
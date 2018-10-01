def part(myls,num):
        t = 0
        p = 0
        while ((t <= num) and (p<len(myls))):
                t = t + myls[p]
                p = p + 1
        if (t <= num) and (p==len(myls)):
                return (myls,[])
        else:
                return (myls[0:p-1],myls[p-1:])

def makemoney(count,cap,people):
	mymoney = 0
	temp = people
	for k in range(count):
		p = part(temp, cap)
		mymoney = mymoney + sum(p[0])
		temp = p[1]+p[0]
	return mymoney







myin = open("c.in")
myout = open("c.out","w")
inputnum = int(myin.readline().strip())
for k in range(1,inputnum+1):
	info = myin.readline().strip().split()
	peop = myin.readline().strip().split()
	newp = [int(t) for t in peop]
	themoney = makemoney(int(info[0]), int(info[1]), newp)
	myout.write("Case #")
	myout.write(str(k))
	myout.write(": ")
	myout.write(str(themoney))
	myout.write("\n")
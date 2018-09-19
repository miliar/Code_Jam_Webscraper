def checkijk(inp):
	a=1
	index,found=find("i",inp)
	if(found==0):
		return "NO"
	inp=inp[index:]
	index,found=find("j",inp)
	if(found==0):
		return "NO"
	inp=inp[index:]
	found=findk(inp)
	if(found==0):
		return "NO"
	return "YES"
def find(ch,inp):
	sign=1
	a="1"
	for i in range(len(inp)):
		b=inp[i]
		temp=product(a,b)
		if temp[0]=="-":
			sign=-sign
			temp=temp[1]
		if(temp==ch and sign==1):
			return i+1,1
		a=temp
	return 0,0
def findk(inp):
        sign=1
        a="1"
        for i in range(len(inp)):
                b=inp[i]
                temp=product(a,b)
                if temp[0]=="-":
                        sign=-sign
                        temp=temp[1]
                a=temp
	if(temp=="k" and sign==1):
        	return 1
        return 0

def product(a,b):
	items=["1","i","j","k"]
	a=items.index(a)
	b=items.index(b)
	product=[["1","i","j","k"],["i","-1","k","-j"],["j","-k","-1","i"],["k","j","-i","-1"]]
	return product[a][b]
testcases=int(raw_input())
out=open("outputC","w")
for i in range(testcases):
	l,x=map(int,raw_input().split(" "))
	st="".join(raw_input()*x)
	result=checkijk(st)
	out.write("Case #"+str(i+1)+": "+result+"\n")
out.close()

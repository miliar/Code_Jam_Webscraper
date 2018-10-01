
def readinput():
	global t
	global inp
	i=0
	for line in open('B-small-attempt0.in'):
		if i==0:
			t=int(line)
			i=1
		else:
			st = line.replace('\n','')
			inp.append(int(st))

def readfromfile():
	global data
	for line in open('precomputed.txt'):
		line=line.replace('\n','')
		data.append(int(line))

def findsmallnum(num):
	global data
	ma=data[0]
	for item in data:
		if item <= num:
			ma=item
		else:
			return ma	 

if __name__=='__main__':
	global res
	global inp
	global data
	inp=[]
	res=[]
	data=[]
	global t
	t=1
	readfromfile()
	readinput()
	print inp,data,t
	for _ in range(t):
		num=inp[_]
		numsmaller=findsmallnum(num)
		res.append(str(numsmaller))
	# for item in res:
	# 	print item
	i=1
	with open('outputsmall2.txt','a') as myfile:
		for item in res:
			myfile.write("Case #"+str(i)+": "+item+"\n")
			i+=1




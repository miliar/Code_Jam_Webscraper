import sys

vowels = ["a","e","i","o","u"]

def probA(string,n):
	n=int(n)
	count=0
	s=0
	e=n+s
	while(s<len(string)-n+1):
		nums=0
		for i in xrange(s,e):
			if string[i] not in vowels:
				nums+=1
			else:
				nums=0
			if nums>=n:
				count+=1
				break 
		e+=1
		if e>len(string):
			s+=1
			e=n+s

	return count

f = open(sys.argv[1],"r")
g = open("result","w")
data = f.readline()
data = f.readline()
times=1
while(data):
	temp = data.split()
	g.write("Case #"+str(times)+": "+str(probA(temp[0],temp[1]))+"\n")
	data = f.readline()
	times+=1

f.close()
g.close()

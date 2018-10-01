from collections import Counter
output=list()
def Problem1():
	f=open('input1.txt');
	n=f.readline()
	print(n)
	for i in range(int(n)):
		inp=f.readline().split()
		output.append(calc(list(inp[0]),int(inp[1])))
	f.close()
	writeOutput()

def calc(s,t):
	#print(s)
	c=0
	for i in range(len(s)-t+1):
		if s[i]=='-':
			c+=1
			for j in range(t):				
				if s[i+j]=='-':
					s[i+j]='+'
				else:
					s[i+j]='-'
	#print(Counter(s))
	if(len(list(Counter(s).keys()))==1):
		return c
	else:
		return 'IMPOSSIBLE'


def writeOutput():
	f=open('output1.txt','w')
	for i in range(len(output)):
		f.write("Case #"+str(i+1)+": "+str(output[i])+'\n')
	f.close()

Problem1()
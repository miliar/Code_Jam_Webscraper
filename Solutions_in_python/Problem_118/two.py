import math
arr = [1,4,9,121,484]

def fns(k):
	if k in arr: return True
	return False
def process(i, j):
	count =0
	for k in range(i, j+1):
		if(fns(k)): 
			count+=1
	return count
with open("test.txt","r") as fs:
	T = int(fs.readline())
	for i in range(0,T):
		s = fs.readline()
		s = s.strip()
		k = s.split(" ")
		k[0] = int(k[0])
		k[1] = int(k[1])
		result = process(k[0], k[1])
		strres = "Case #"+str(i+1)+": "+str(result)
		print strres
	

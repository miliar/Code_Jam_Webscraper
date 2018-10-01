import math

def palin(word):
	if(len(word)%2 == 0):
		fp, sp = word[:len(word)/2],word[len(word)/2:]
	else:
		fp, sp = word[:len(word)/2],word[(len(word)/2)+1:]
	return fp == sp

if __name__ == "__main__":
	ct = int(raw_input())
	for j in range(ct):
		s, e = raw_input().split()
		s = int(s)
		e = int(e)
		result = 0
		for i in range(s,e+1):
			if(palin(str(i))):
				if(math.floor(math.sqrt(i))**2 == i):
					if(palin(str(int(math.sqrt(i))))):
						result += 1
		print "Case #"+str(j+1)+": "+str(result)
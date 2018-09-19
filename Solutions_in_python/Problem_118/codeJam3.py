import math

def isFair(a):
	return str(a) == str(a)[::-1]

if __name__=="__main__":
	inputNum = int(raw_input())

	tab = {}

	for i in range(1,inputNum+1):
		inp = raw_input()
		a,b = inp.split(" ")
		a,b = int(math.ceil(math.sqrt(int(a)))), int(math.floor(math.sqrt(int(b))))
		count = 0
		for x in range(a, b+1):
			if x**2 not in tab:
				if isFair(x) and isFair(x**2):
					tab[x**2] = 1
				else:
					tab[x**2] = 0
			count += tab[x**2]
		print("Case #%d: %d" % (i, count))
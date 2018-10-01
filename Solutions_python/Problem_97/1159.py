#!/usr/bin/python3
def main():
	fh = open('C-small-attempt0.in')
	T = 0
	for line in fh:
		if T != 0:
			A = int(line.split()[0])
			B = int(line.split()[1])
			ret = 0
			mem = []
			for i in range(B):
				mem.append(0)
			
			for i in range(B + 1):
				if i >= A and mem[i-1] == 0:
					val = 1
					k = i
					while True:
						wine = int(str(k)[1:] + str(k)[:1])
						if len(str(wine)) == len(str(k)):
							k = wine
							if k == i:
								break
							if k >= A and k <= B:
								mem[k-1] = 1
								val = val + 1
						else:
							k = str(k)[1:] + str(k)[:1]
					ret = ret + val * (val-1) / 2
						
			print('Case #' + str(T) + ':', int(ret))
		T = T + 1

main()





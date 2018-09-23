import sys

f = open(sys.argv[1], 'r')
out = open(sys.argv[2], 'w')
out.close()
rl = lambda: f.readline()
line_n = int(rl())

for i in range(line_n):
	r_line = rl().strip()
	n, k= r_line.split(" ")
	n, k=int(n), int(k)
	numdic = {n:1}
	if n==k:
		maxset, minset = 0, 0
	else:
		h = 0
		while h < k:
			maxNum = max(list(numdic.keys()))
			countMax = numdic[maxNum]
			numforCal =  int(maxNum)
			absNum =  int((numforCal-1)/2)
			secNum =  numforCal-absNum-1
			if absNum in numdic.keys():
				Valcount = numdic[absNum] + countMax
				numdic[absNum] = Valcount
			else:
				numdic[absNum] = countMax
			if secNum in numdic.keys():
				Valcount = numdic[secNum] + countMax
				numdic[secNum] = Valcount
			else:
				numdic[secNum] = countMax
			del numdic[maxNum]
			maxset, minset = secNum, absNum
			h=h+countMax
	result = str(maxset) + " " + str(minset)
	resultforWrite = "Case #%s: " % (i+1) + result+"\n"
	out = open(sys.argv[2], 'a')
	out.write(resultforWrite)
	out.close()
f.close



fo = fo = open("B-large.in","r+")
fw = open("output.txt","w")
def ToInt(str):
	return int(str.strip())


count = ToInt(fo.readline())


for i in range(1,count+1):
	total = 0.0
	measures = [float(s) for s in fo.readline().strip().split()]

	K = 10000000
	G = measures[0]
	F = measures[1]
	X = measures[2]
	results = [X/2]

	for j in range(1,K+1):
		total = total + G / (2.0+F*(j-1))
		results.append(total + X / (2.0+F*j))

	fw.write("Case #{0}: {1}\n".format(i,min(results)))


fo.close()
fw.close()
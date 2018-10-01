infile = open("in.in", "r")
lines = infile.readlines()
outfile = open("out.out", "w")
tc = int(lines[0])


for t in range(tc):
	(n, k) = [int(each) for each in lines[t+1].strip().split()]
	p = [0 for each in range(n+2)]
	p[0] = 1
	p[n+1] = 1

	for i in range(k):
		p1 = 0
		p2 = 0
		ist = 0

		#find 1 from 1 to n+1 in p, and find interval i1 to i2
		for j in range(1, len(p)):
			if p[j] == 1:
				if (j - ist) > (p2 - p1):
					p1 = ist
					p2 = j
				ist = j
		
		pos = int((p2 + p1)/2)
		p[pos] = 1
		#print(p)
		if i == k-1 :
			outfile.write("Case #" + str(t+1) + ": " + str(p2 - pos - 1) +  " " + str(pos - p1 - 1) + "\n")



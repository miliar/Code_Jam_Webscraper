from math import log, exp, floor, ceil

finput = open("csmall.in", "Ur")
foutput = open("csmall.out", "w")

testCases = int(finput.readline())

for i in xrange(1, testCases+1):
	line = finput.readline()
	line = line.rstrip()
	line = line.split(' ')
	A = int(line[0])
	B = int(line[1])
	count = 0
	a = exp(0.5*log(A))	
	b = exp(0.5*log(B))
	for q in xrange(int(floor(a)), int(ceil(b))+1):
		s = q*q	
		if s >= A and s <= B:
			reverse = 0
			temp = s
			while (temp > 0):
				last = temp % 10
				reverse = reverse * 10 + last
				temp = temp / 10
		
			if s == reverse:
				temp = q
				reverse = 0
				while (temp > 0):
					last = temp % 10
					reverse = reverse * 10 + last
					temp = temp / 10
		
				if q == reverse:
					count += 1			
				
	if (i < testCases):
		foutput.write("Case #"+str(i)+": "+str(count)+"\n")
	else:
		foutput.write("Case #"+str(i)+": "+str(count))
finput.close()
foutput.close()

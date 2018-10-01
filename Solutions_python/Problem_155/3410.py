import sys

line = sys.stdin.readline().rstrip()
cases = int(line)
#print "Cases: "+ str(cases)
case = 1

line = sys.stdin.readline().rstrip()
pos = line.find(' ')
size = int(line[0:pos])

while line:
	line = line[pos+1:]
	#print "Typed: "+ line
	n = 0
	t = 0
	for i in range(0,len(line)):
		s = int(line[i])
		#print "i="+str(i)+", s="+str(s)+", t="+str(t)+", n="+str(n)
		if t<i and s>0:
			n += (i-t)
			s += (i-t)
			#print "--> sum "+ str(i-t) + ", n="+str(n)
		t = t+s
	print "Case #"+str(case)+": " + str(n)


	line = sys.stdin.readline().rstrip()	
	if line:
		pos = line.find(' ')
		#print "-->"+line[0:pos]
		size = int(line[0:pos])
	case += 1

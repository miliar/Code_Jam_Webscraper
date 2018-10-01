#/bin/env/python
import fractions
f = open("in", "rb")
t = int(f.readline())
for tt in range(t):
	print "Case #"+str(tt+1)+": ",
	n,pd,pg = map(int, f.readline().split(" "))
	dd, gg = [float( pd)/100, float( pg)/100]
	if (dd!= 1.0 and gg == 1.0):
		print "Broken"
		continue
	if (dd + gg == 0):
		print "Possible"
		continue
	if (100/fractions.gcd(pd,100) or pd/fractions.gcd(pd,100)) > n:
		print "Broken"
		continue
	if (dd != 0 and gg == 0):
		print "Broken"
		continue
	
	print "Possible"

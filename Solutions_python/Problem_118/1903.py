#!/usr/bin/env python
import math
import numpy as np

textfile = open("palin.in")
lines = [line.strip() for line in textfile]
textfile.close()
textfile = open("pal.out","w")
numCases = int(lines[0].split()[0])
for i in range(0,numCases,1):
	rangelist = list(lines[i+1].split())
	startn = int(rangelist[0])
	endn = int(rangelist[1])

	sqrt_startn = int(math.ceil(math.sqrt(long(startn))))
	sqrt_endn = int(math.floor(math.sqrt(long(endn))))
	count = 0
#	print "{s} to {t}".format(s=startn,t=endn);
#	print "{s} to {t} (sqrt)".format(s=sqrt_startn,t=sqrt_endn);

	for x in range(sqrt_startn,sqrt_endn+1,1):
		if(str(x)[::-1] == str(x) and (str(x*x))[::-1] == str(x*x)):
			print "   sqr: {s}".format(s=x*x)
			count = count + 1
#	print "count: {c}".format(c = count)
	textfile.write("Case #{c}: {ans}\n".format(c = i+1,ans = count))
textfile.close()

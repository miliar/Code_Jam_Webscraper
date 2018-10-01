#!/usr/bin/env python

import sys

InGooglerese = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"
InEnglish = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"

infile = sys.stdin
t = int(infile.readline())
for j in xrange(t):
	out=""
	values=list(infile.readline()) 
	for i in xrange(len(values)-1):
			sindex=InGooglerese.find(values[i])
			if sindex != -1:
				out=out+InEnglish[sindex]
			elif values[i] is "z":
				out=out+"q"
			elif values[i] is "q":
				out=out+"z"
	print("Case #%d: %s" % (j+1, out))

#!/usr/bin/env python

import sys;
import string;

N = int(sys.stdin.readline());

alpha=list(string.digits);
alpha += list(string.letters);
alpha[1]='0';
alpha[0]='1';

def frombx_tobase10(b,n):
	n.reverse();
	pos = 0;
	res = 0 ;
	for c in n:
		if c in string.digits:
			res += int(c)*(b**pos);
		else:
			res += alpha.index(c)*(b**pos);
		pos = pos +1;
	return res;

for i in xrange(N):
        number = sys.stdin.readline().strip();
        digits = list(number);
	idx = 0;
	trans={};
	traducted="";
	for c in digits:
		if trans.has_key(c):
			traducted += trans[c]	;
		else:
			trans[c]=alpha[idx];
			traducted += alpha[idx];
			idx = idx + 1;
	base=max(2,idx);
	print "Case #%d: %d" % (i+1,frombx_tobase10(base,list(traducted)))
	

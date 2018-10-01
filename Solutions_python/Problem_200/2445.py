#!/usr/bin/python
################################################################
#	Author:	Khalil Sawant
# https://code.google.com/codejam/contest/3264486/dashboard#s=p1
################################################################

import sys;

T = int(raw_input());

for i in range(T):

	N = list(str(raw_input()));
	noOfDigits = len(N);

	while True:
		inversion = False;
		for j in range(noOfDigits-1):
			if (N[j] > N[j+1]):
				inversion = True;
				N[j] = chr(ord(N[j])-1);
				for k in range(noOfDigits-1-j):
					N[j+k+1] = '9';

		if not inversion:
			break;

	print("Case #%d: %s" %(i+1, "".join(N).lstrip('0') ) );

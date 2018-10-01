#!/usr/bin/python

T = int(raw_input());
for caseN in range(1,T+1):
	N = int(raw_input());
	wires = {}
	for ln in range(N):
		(A,B) = map(int,raw_input().split());
		wires[A] = B;
	#print wires.keys()
	k = wires.keys()
	k.sort();
	count = 0;
	for wire in k:
		for wireB in [A for A in k if A > wire]:
			#print wire, wireB;
			if wires[wire] > wires[wireB]:
				count+=1;
	print "Case #{0}: {1}".format(caseN,count);


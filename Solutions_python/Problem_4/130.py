#!/usr/bin/env python

#!/usr/bin/env python

import sys;
import operator;

def solve (v1, v2):
	v1.sort();
	v2.sort();
	v2.reverse();
	#v3 = [x*y for x in v1, y in v2];
	v3 = map(operator.mul, v1, v2);
	return sum(v3);


#sys.stdin = open("Text-1.txt");
lines = sys.stdin.readlines();
it = iter(lines);

cmax = int(it.next().rstrip());
cidx = 1;
while cidx <= cmax:
	vno = int(it.next().rstrip());
	sv1 = it.next().rstrip().split();
	sv2 = it.next().rstrip().split();
	v1 = [int(x) for x in sv1];
	v2 = [int(x) for x in sv2];
	rz = solve(v1, v2);
	print "Case #%d: %d" % (cidx, rz);
	cidx += 1;

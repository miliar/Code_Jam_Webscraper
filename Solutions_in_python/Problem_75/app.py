#! /usr/bin/env python
from collections import deque

def combining_els(parts):
	els = {}
	count = int(parts.popleft())
	for i in xrange(count):
		tri = parts.popleft()
		els[tri[:2]] = tri[2]
		
	return els
	
def opposing_els(parts):
	els = []
	count = int(parts.popleft())
	for i in xrange(count):
		els.append(list(parts.popleft()))
		
	return els
	
def process_line(line):
	parts = deque(line.split())
	c_els = combining_els(parts)
	o_els = opposing_els(parts)
	orig_len = int(parts.popleft())
	orig_str = parts.popleft()
	
	test = ""
	for c in orig_str:
		test += c
		
		# Look for combining
		for pair, pair_comb in c_els.items():
			test = test.replace(pair, pair_comb).replace(pair[::-1], pair_comb)
				
		# Look for opposing
		for opp in o_els:
			if test.find(opp[0]) > -1 and test.find(opp[1]) > -1:
				test = ""
	
	return list(test)
		

f = open("in.txt", "r")
num_lines = int(f.readline())
for i in xrange(num_lines):
	print ("Case #%d: %s" % (i + 1, process_line(f.readline()))).replace("'", "")
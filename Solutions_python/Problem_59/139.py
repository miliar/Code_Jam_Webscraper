#!/usr/bin/python
#
# Google Code Jam
#
#

import sys
import os

debug=False

def solve_test_case(N,M,current_paths,new_paths):
	current_paths.sort()
	new_paths.sort()
	cparray = []
	for cp in current_paths:
		p = cp.split('/')
		if len(p[0]) == 0: p=p[1:]
		if len(p[-1]) == 0: p=p[0:-1]
		cparray.append(p)
		if debug:
			print "adding path:"
			print cp
			print p
			print ""

	paths = set()
	for cp in cparray:
		path = []
		for dir in cp:
			path.append(dir)
			npath = []
			npath.extend(path)
			paths.add(tuple(npath))

	if debug: 
		print "paths:", paths
			
	nparray = []
	for np in new_paths:
		p = np.split('/')
		if len(p[0]) == 0: p=p[1:]
                if len(p[-1]) == 0: p=p[0:-1]
		if debug:
			print "nparray adding:"
			print p
		nparray.append(p)

	mkdir = 0
	for np in nparray:
		for i in xrange(0,len(np)):
			dir = tuple(np[0:i+1])
			if not dir in paths:
				mkdir += 1
				paths.add(dir)

	return mkdir
				
				
				 
	

if __name__ == '__main__':
    input = open(sys.argv[1])
    if len(sys.argv) > 2 and sys.argv[2] == "--debug": debug=True
    test_case_count = int(input.readline().strip())
    test_case = 0
    while test_case < test_case_count:
	N,M = map(int, input.readline().strip().split())
	current_paths = []
	while len(current_paths) < N:
		current_paths.append(input.readline().strip())
	new_paths = []
	while len(new_paths) < M:
		new_paths.append(input.readline().strip())
        test_case += 1
        print "Case #%d: %s" % (test_case, solve_test_case(N,M, current_paths, new_paths))


 
            
 

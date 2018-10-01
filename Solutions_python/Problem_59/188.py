from sys import *

def solve(i, dirs, ndirs):
	
	n_mkdirs = 0
	
	for x in ndirs:
		sdirs = x.split('/')
		sdirs = sdirs[1:]
		dir = ""
		root_dir = True
		for y in sdirs:
			dir += "/"+y
			#print dir
			if (not root_dir) or (dir not in dirs):
				n_mkdirs += 1
				dirs.append(dir)
				root_dir = False
		
	print "Case #%d: %s" %(i+1, n_mkdirs)
	

n_cases = int(raw_input())
for i in xrange(n_cases):
	N, M =  map(int, stdin.readline().split())
	dirs = []
	for n in xrange(N):
		dirs.append(raw_input())
	#print dirs
	ndirs = []
	for m in xrange(M):
		ndirs.append(raw_input())
	#print ndirs
	solve(i, dirs, ndirs)
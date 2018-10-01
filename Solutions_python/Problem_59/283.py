#!/usr/bin/env python

import sys

class Tree:
    def __init__(self):
	self.subtrees = {}
    def create_path(self, path):
	#print 'create', path
	if len(path) == 0:
	    return 0
	try:
	    return self.subtrees[path[0]].create_path(path[1:])
	except KeyError:
	    #print 'mkdir', path[0]
	    self.subtrees[path[0]] = Tree()
	    return 1 + self.subtrees[path[0]].create_path(path[1:])

filename=sys.argv[1]
inputfile=file(filename, 'r')
numcases=int(inputfile.readline().strip())
for case in range(1,numcases+1):
    N, M = map(long, inputfile.readline().strip().split())
    exist=[]
    for k in range(N):
	exist.append(inputfile.readline().strip().split('/')[1:])
    create=[]
    for k in range(M):
	create.append(inputfile.readline().strip().split('/')[1:])

    filesystem = Tree()
    for path in exist:
	filesystem.create_path(path)
    mkdirs = 0
    for path in create:
	mkdirs += filesystem.create_path(path)

    print "Case #%d: %d" % (case, mkdirs)

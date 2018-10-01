import sys, os, itertools
from math import sqrt

def grouper(n, iterable, fillvalue=None):
    args = [iter(iterable)] * n
    return itertools.izip_longest(fillvalue=fillvalue, *args)

def isPal(n):
	o=list(str(n))
	r=o[:]
	r.reverse()
	return r==o

nums = []
lines = open(sys.argv[1]).readlines()[1:]
for i,line in enumerate(lines):
	nums.extend(line[:-1].split(' '))
nums = map(int,nums)
all_fs = filter(isPal,[i* i for i in filter(isPal,range(int(sqrt(max(nums)))+2))])
i=0
fo = open('Cout.txt','w+')
for s,e in grouper(2,nums):
	i+=1
	print >>fo,"Case #%s: %s" % (i,len(set(range(s,e+1)).intersection(all_fs)))

	

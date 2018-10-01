import sys
sys.path.append('../..')
from codejam import get, result

def column(matrix, i): # http://stackoverflow.com/questions/903853/how-to-extract-column-from-a-multi-dimentional-array
    return [row[i] for row in matrix]

def tryMow(n,m,pattern):
	lawn=[[100]*m]*n
	for x in range(n): # Mow across
		h=max(pattern[x])
		lawn[x]=[min(h,i) for i in lawn[x]]
	for y in range(m): # Mow down
		h=max(column(pattern,y))
		for x in range(n):
			lawn[x][y]=min(h,lawn[x][y])
	return lawn

cases=get.int()
for iCase in range(cases):
	n,m=get.intList()
	pattern=[[int(i) for i in s.split()] for s in get.strLines(n)]
	if tryMow(n,m,list(pattern)) == pattern:
		result(iCase,"YES")
	else:
		result(iCase,"NO")

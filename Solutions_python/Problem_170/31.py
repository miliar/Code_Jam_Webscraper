from sys import stdin
import sys
import itertools

fin = stdin

T = int(fin.readline())

sets = []
ans = 0

def dfs(n, lim, set1_n, set2_n):
	global ans
	global se
	if n == lim:
		nans = len( set1_n & set2_n )
		if nans < ans:
			ans = nans
		return
	if len( set1_n & set2_n ) > ans:
		#print >> sys.stderr, "broke at %d" % (n)
		return
	if n%2 == 0:
		dfs(n+1, lim, set1_n|sets[n], set2_n)
		dfs(n+1, lim, set1_n, set2_n|sets[n])
	else:
		dfs(n+1, lim, set1_n, set2_n|sets[n])
		dfs(n+1, lim, set1_n|sets[n], set2_n)

for tc in xrange(T):
	n = int(fin.readline())
	set1 = set( fin.readline()[:-1].split(' ') )
	set2 = set( fin.readline()[:-1].split(' ') )
	sets = []
	for i in range(n-2):
		setn = set( fin.readline()[:-1].split(' ') )
		sets.append( setn )
	ans = 10000 * n
	dfs(0,len(sets),set1,set2)
	print "Case #%d: %d" % (tc+1, ans)
	print >> sys.stderr, "Case #%d: %d" % (tc+1, ans)

import sys

ans = {}
f = open( "smallcases.txt")
for l in f:
	l = l.split()
	n,m,k,a = [int(x) for x in l]
	ans[(n,m,k)] = a
f.close()

f = open( sys.argv[1] )
f.readline()
l = f.readline()
casenum = 1
while l != "":
	n,m,k = [int(x) for x in l.split()]

	a = min(n,m)
	b = max(n,m)

	try:
		output = ans[(a,b,k)]
	except KeyError:
		output = k

	print "Case #{}: {}".format(casenum,output)
	casenum += 1

	l = f.readline()
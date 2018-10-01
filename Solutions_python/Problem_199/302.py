import sys

T = int(sys.stdin.readline())

for tc in xrange(1, T + 1):
    line, K = sys.stdin.readline().split()
    K = int(K)
    
    line = list(line)
    ans = 0
    for i in xrange(len(line) - K + 1):
	if line[i] == '-':
           ans += 1

	   for j in xrange(K):
	      line[i + j ] = '-' if line[i + j] == '+' else '+'


    line = "".join(line)
    if line.find('-') > 0:
	print "Case #%d: IMPOSSIBLE" % tc
    else:
	print "Case #%d: %d" % (tc, ans)

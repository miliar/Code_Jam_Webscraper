import sys

def solve(N, K):
	max_val = N / 2
	min_val = N / 2
	if N % 2 == 0:
		min_val = (N / 2) - 1

	if K == 1:
		return (max_val, min_val)
	temp = min_val
	if K % 2 == 0:
		temp = max_val
	return solve(temp, K / 2)

lines = [x for x in open(sys.argv[1], 'rt').readlines()]
count = int(lines.pop(0))
with open('out.txt', 'wt') as outfile:
	for i in xrange(count):
		N, K = [int(x) for x in lines.pop(0).strip().split(' ')]
		max_res, min_res = solve(N, K)
		print 'Case #%d: %s %s' % (i + 1, max_res, min_res)
		outfile.write('Case #%d: %s %s\n' % (i + 1, max_res, min_res))

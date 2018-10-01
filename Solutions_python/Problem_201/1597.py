from math import log, floor, ceil

def main():
	num_tests = int(input())
	for case in range(num_tests):
		n, k = [int(x) for x in input().split()]
		M, m = solve(n, k)
		print('Case #{}: {} {}'.format(case+1, M, m))


def solve(n, k):
	if k == 1:
		vacant = n - 1
		return ceil(vacant/2), floor(vacant/2)

	k0 = 2**floor(log(k, 2)) - 1
	k1 = k - k0
	n1 = n - k0
	m = n1 // (k0+1)
	r = n1 % (k0 + 1)
	size = m + (k1 <= r)
	vacant = size-1
	
	return ceil(vacant/2), floor(vacant/2)



main()
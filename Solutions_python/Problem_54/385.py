import fractions 
import string
import sys
def abs(a):
	if a > 0:
		return a
	return -a
def solve(argv = sys.argv):
	in_file = open(argv[1])
	lines = in_file.readlines()
	C = int(lines[0])
	for li_no in range(C):
		sp = string.split(lines[li_no + 1])
		N = int(sp[0])
		t = map(int, sp[1:1+N])

		T = abs(t[0] - t[1])

		for j in range(N):
			for k in range(j + 1, N):
				T = fractions.gcd(T, abs(t[j] - t[k]))
		
		ans = T - t[0] % T
		flag = 0
		for tt in t:
			if tt % T == 0:
				flag += 1

		if flag == N:
			ans = 0
		print "Case #%d: %d"%(li_no + 1, ans)

	in_file.close()
if __name__ == "__main__":
	solve()


import os
import math

def read_input():
	file_name = "%s/small.in" % os.getcwd()
	return open(file_name, "r")

def make_output(ans):
	file_name = "%s/small.out" % os.getcwd()
	f = open(file_name, "w")
	f.write(ans)
	f.close()

def get_ans(N, case):
	M = [x for x in range(N+1)]
	for i in range(10, N+1):
		rev = int(str(i)[::-1])
		revrev = int(str(rev)[::-1])
		if revrev != i or rev >= i:
			M[i] = 1 + M[i-1]
		else:
			M[i] = 1 + min(M[i-1], M[rev])
	ans = M[N]
	return "Case #%d: %d\n" % (case, ans)

def main():
	ans = ""
	f = read_input()
	T = int(f.readline())
	for i in range(T):
		print i
		N = int(f.readline())
		ans += get_ans(N, i+1)
	f.close()
	make_output(ans)

main()

print get_ans(1, 1)
print get_ans(19, 1)
print get_ans(23, 1)
inf = open("C-small-attempt0.in")
ouf = open("C-small-attempt0.out", "w")

testNo = int(inf.readline())

def good(x, y):
	tx = str(x)
	ty = str(y)
	for i in range(0, len(tx)):
		if tx[i:]+tx[:i] == ty:
			return True
	return False


for test in range(1, testNo + 1):
	a, b = [int(x) for x in inf.readline().split()]

	ans = 0
	for n in range(a, b + 1):
		for m in range(n + 1, b + 1):
			if good(n, m):
				ans = ans + 1

	ouf.write("Case #" + str(test) + ": " + str(ans) + "\n")

ouf.close()
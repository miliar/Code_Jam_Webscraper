import sys
file = sys.stdin

def cycled(x):
	x_str = str(x)
	return (int(x_str[n:] + x_str[:n]) for n in range(len(x_str)))

for i in range(0, int(file.readline().strip())):
	A, B = (int(n) for n in file.readline().strip().split(' '))
	recycled = set()
	for n in range(A, B):
		recycled.update((n, x) for x in cycled(n) if x > n and x <= B);
	print("Case #%d: %d" % (i + 1, len(recycled)))

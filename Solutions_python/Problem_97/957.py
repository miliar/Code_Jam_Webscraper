def check(a, b):
	a, b = str(a), str(b)
	c = a[1:] + a[0]
	while c != a:
		if c == b:
			return True
		c = c[1:] + c[0]
	return False

def main():
	input = open("C-small-attempt0.in", "r").readlines()
	T = int(input[0])
	for t in range(1, T + 1):
		count = 0 
		ints = input[t].split()
		A, B = int(ints[0]), int(ints[1])
		for a in range(A, B):
			for b in range(a + 1, B + 1):
				if check(a, b):
					count += 1
		print "Case #%d: %d" % (t, count)

if __name__ == "__main__":
	main()

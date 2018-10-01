g_bad = False

def calculate_last_number(N):
	global g_bad

	while N > 0:
		g_bad = False
		digits = [int(c) for c in str(N)]
		#print digits

		if len(digits) == 1:
			return N

		for i in range(len(digits) - 1, 0, -1):
			#print "{0} vs {1}".format(digits[i - 1], digits[i])
			if digits[i - 1] > digits[i]:
				g_bad = True

		if g_bad == False:
			return N
		else:
			N -= 1

def main():

	f = open("B-small-attempt0.in")
	lines = f.readlines()
	T = int(lines[0])

	for i in range(1, T + 1):
		print "Case #{0}: {1}".format(i, calculate_last_number(int(lines[i])))

if __name__ == "__main__":
	main()


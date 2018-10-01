def main():
	f = open("B-large.in", "r")
	out = open("out.txt", "w")
	T = f.readline()
	j = 1
	for line in f:
		nums = line.split()
		N = int(nums[0])
		global S, p
		S = int(nums[1])
		p = int(nums[2])
		maxG = 0
		for i in range(3, len(nums)):
			tP = int(nums[i])
			maxG += scanPossible(tP)
		out.write("Case #" + str(j) + ": " + str(maxG) + "\n")
		j += 1

def scanPossible(tP):
	global S, p
	for b in range((tP-2)/3, (tP+2)/3 + 1):
		for c in range(b-2, b+1):
			for a in range(b, b+3):
				if a + b + c != tP or a - c > 2:
					continue
				if a - b != 2 and b - c != 2 and a - c != 2 and a >= p and c >= 0:		
					return 1
	for b in range((tP-2)/3, (tP+2)/3 + 1):
		for c in range(b-2, b+1):
			for a in range(b, b+3):
				if a + b + c != tP or a - c > 2:
					continue
				if (a - b == 2 or b - c == 2 or a - c == 2) and a >= p and S > 0 and c >= 0:
					S -= 1
					return 1
	return 0
	
if __name__ == "__main__":
	main()

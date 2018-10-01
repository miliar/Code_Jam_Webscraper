import sys

def findSolution(case, S_s):
	C_s = []
	additional = 0
	currCount = 0
	for i in range(len(S_s)):
		if i == 0:
			currCount += S_s[i]
			continue
		if currCount < i and S_s[i] > 0:
			additional += i - currCount
			currCount += additional
		currCount += S_s[i]
	return (case, additional)

if __name__=="__main__":
	lines = open(sys.argv[1]).readlines()
	lines = [line.strip() for line in lines]
	T = int(lines[0])
	case = 1
	for line in lines[1:]:
		parts = line.split(" ")
		S_max = int(parts[0])
		
		S_s = []
		i = 0
		for c in parts[1]:
			S_s += [int(c)]
		solution = findSolution(case, S_s)
		print "Case #%d: %d"%(solution[0], solution[1])
		case += 1
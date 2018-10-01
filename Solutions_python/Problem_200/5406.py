allTidy = []

def getAllTidy():
	for x in xrange(1, 1000):
		temp = [i for i in str(x)]
		temp.sort()
		temp = ''.join(temp)
		if str(x) == temp:
			allTidy.append(x)

def bst(lo, hi, N):
	if hi == lo:
		if allTidy[lo] <= N:
			return allTidy[lo]
		return allTidy[lo - 1]
	mid = (((hi - lo) / 2) + lo) + 1
	if allTidy[mid] == N:
		return allTidy[mid]
	if allTidy[mid] > N:
		return bst(lo, mid-1, N)
	return bst(mid, hi, N)

def solve(N) :
	return bst(0, len(allTidy) - 1, N)

getAllTidy()

#T = int(raw_input())
#for test in xrange(T):
#	N = int(raw_input())
#	case = test + 1
#	print "Case #", case, ": ",solve(N)

with open('B-small-attempt1.in') as f:
	with open('tidy_out.txt' , 'w') as out:
		T = int(f.readline().strip())
		for test in xrange(T):
			N = int(f.readline())
			case = test + 1
			out.write("Case #" + str(case) + ": " + str(solve(N)))
			out.write("\n")

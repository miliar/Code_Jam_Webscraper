def parse_matrix(n):
	b = []
	for i in xrange(n):
		b.append(map(int,raw_input().split()))
	return b
	
def row_check(b,row):
	maximum = max(b[row])
	m = len(b)
	n = len(b[0])
	for index in xrange(n):
		x = b[row][index]
		if x < maximum:
			for col in xrange(m):
				if b[col][index] > x:
					return False
	return True
	
def mat_check(b):
	for i in xrange(len(b)):
		if not row_check(b,i):
			return False
	return True
	
if __name__ == "__main__":
	trials = int(raw_input())
	file = open("output.txt",'w')
	for x in xrange(1,trials+1):
		file.write("Case #%i: " % x)
		n = int(raw_input().split()[0])
		mat = parse_matrix(n)
		if mat_check(mat):
			file.write("YES\n")
		else:
			file.write("NO\n")
	file.close()
		
	
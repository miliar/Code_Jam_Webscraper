import fileinput

def solve(r1, m1, r2, m2):
	a = set(m1[r1-1]) & set(m2[r2-1])
	if a:
		return min(a) if len(a) == 1 else "Bad magician!"
	else:
		return "Volunteer cheated!"

f = fileinput.input()
for t in range(1, 1+int(f.readline())):
	r1 = int(f.readline())
	m1 = [list(map(int, f.readline().rstrip().split())) for i in range(4)]
	r2 = int(f.readline())
	m2 = [list(map(int, f.readline().rstrip().split())) for i in range(4)]
	print("Case #%d: %s" % (t, solve(r1, m1, r2, m2)))
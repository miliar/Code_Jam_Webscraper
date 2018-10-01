import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10**6)


def read_file():
	f = open('input.txt')
	c = f.readlines()

	tests = []
	test_num = int(c[0])
	for i in range(1, test_num+1):
		s = c[i].split(' ')

		t = []
		for ct in s:
			t.append(float(ct))
		tests.append(t)

	return test_num, tests

def routine(diff, c, f, x):

	t1 = x / diff
	t2 = c / diff + x / (diff + f)

	if t1 <= t2:
		return t1

	all_sec = c / diff
	new_diff = diff + f
	return all_sec + routine(new_diff, c, f, x)
		

def run_test(c, f, x):
	diff = 2	
	seconds = routine(diff, c, f, x)
	return seconds


n, t = read_file()
for i in range(0, n):
	sec = run_test(t[i][0], t[i][1], t[i][2])
	print 'Case #{0}: {1}'.format(i+1, sec)


	



import gcj, random

def last_tidy(N):
	SN = str(N)
	if len(SN) == 1:
		return N

	last_tidy = -1
	last_untidy = -1
	for i in range(len(SN) - 1):
		if SN[i] > SN[i + 1]:
			last_tidy   = i
			last_untidy = i + 1
			break

	if last_tidy == -1:
		return N

	first_tidy = last_tidy
	while SN[first_tidy] == SN[last_tidy] and first_tidy >= 0:
		first_tidy -= 1
	first_tidy += 1

	#print("Last tidy = ", SN[last_tidy], "First tidy", SN[first_tidy])

	return int(SN[:first_tidy] + str(int(SN[first_tidy]) - 1) + "9" * (len(SN) - first_tidy - 1))


def tidy(N):
	SN = str(N)
	for i in range(len(SN) - 1):
		if SN[i] > SN[i + 1]:
			return False
	return True

def brute(N):
	last = 0
	for i in range(1, N + 1):
		if tidy(i):
			last = i
	return last

ifile, ofile = gcj.get_files('B')

T = int(ifile.readline().strip())
for t in range(T):
	N = int(ifile.readline())
	#N = random.randint(1, 100000)
	#ans = brute(N)
	#if brute(N) != last_tidy(N):
	#	print("ALARMA", N, brute(N), last_tidy(N))
	ans = last_tidy(N)
	gcj.print_answer(ofile, t, str(ans))
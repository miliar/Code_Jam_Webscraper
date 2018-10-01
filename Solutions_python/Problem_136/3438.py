from sys import argv, setrecursionlimit

setrecursionlimit(100000000)
def get_time(c, f, x, rate = 2):
	time0 = x/rate
	next_frame = c/rate
	next_rate = rate+f
	time1 = next_frame + x/next_rate
	if time0 < time1:
		return time0
	else:
		return next_frame + get_time(c, f, x, next_rate)

with open(argv[1]) as f:
	f.readline()
	i = 1
	for ligne in f:
		c, f, x = tuple(ligne.strip().split(' '))
		best_time = get_time(float(c), float(f), float(x))
		print("Case #%d: %.7f" % (i, best_time))
		i += 1

def _main():
	d, n = raw_input().split(' ')
	d = float(d)
	n = int(n)
	horse = []
	for i in range(0, n):
		k, s = raw_input().split(' ')
		k = float(k)
		s = float(s)
		horse.append((k, s))
	timeMax = []
	for elem in horse:
		k, s = elem
		time = (d - k) / s
		timeMax.append(time)
	timeHorse = max(timeMax)
	v = d / timeHorse
	print '{:.6f}'.format(v)


nbTest = int(raw_input())
for i in range(1, nbTest + 1):
	print "Case #"+ str(i) + ":",
	_main()
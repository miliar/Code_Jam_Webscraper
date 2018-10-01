import sys

def cookieClickerAlpha():
	f = open(sys.argv[1])
	w = open('output.out', 'w')
	T = int(f.readline())
	for case in range(1, T + 1):
		data = f.readline().split()
		C = float(data[0])
		F = float(data[1])
		X = float(data[2])
		rate = 2
		time = 0
		while(isConvinientAFarm(C, F, X, rate)):
			time = time + C / rate
			rate = rate + F
		time += X / rate
		w.write("Case #{0}: {1:.7f}\n".format(case, time))

def isConvinientAFarm(C, F, X, rate):
	if(X / rate > C / rate + X / (rate + F)):
		return True
	else:
		return False

cookieClickerAlpha();
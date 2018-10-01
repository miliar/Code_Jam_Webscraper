import sys

class Trip(object):
	def __init__(self, hh1, mm1, hh2, mm2, start):
		self.t1 = hh1 * 60 + mm1
		self.t2 = hh2 * 60 + mm2
		self.start = start
		self.done = False
	def order(self):
		return self.t1 * 5000 + self.t2
	def __repr__(self):
		if self.start == "A":
			tgt = "B"
		else:
			tgt = "A"
		return "(%s) %d -> %d (%s): %s" % (self.start, self.t1, self.t2, tgt, self.done)

f = open(sys.argv[1])

N = int(f.readline())

for i in xrange(N):
	trips = []
	T = int(f.readline())
	NA, NB = map(int, f.readline().split())
	for j in xrange(NA):
		tA, tB = f.readline().split()
		hhA, mmA = map(int, tA.split(":"))
		hhB, mmB = map(int, tB.split(":"))
		trips.append(Trip(hhA, mmA, hhB, mmB, "A"))
	for j in xrange(NB):
		tB, tA = f.readline().split()
		hhB, mmB = map(int, tB.split(":"))
		hhA, mmA = map(int, tA.split(":"))
		trips.append(Trip(hhB, mmB, hhA, mmA, "B"))
	trips.sort(key=Trip.order)
	n = len(trips)
	ndone = 0
	nA, nB = 0, 0
	while ndone < n:
		readyTime, readyPlace = None, None
		for t in trips:
			if not t.done:
				if readyTime == None:
					if t.start == "A":
						nA += 1
						readyPlace = "B"
					else:
						nB += 1
						readyPlace = "A"
					readyTime = t.t2 + T
					t.done = True
					ndone += 1
				else:
					if readyPlace == t.start and readyTime <= t.t1:
						if t.start == "A":
							readyPlace = "B"
						else:
							readyPlace = "A"
						readyTime = t.t2 + T
						t.done = True
						ndone += 1
	print "Case #%d: %d %d" % (i + 1, nA, nB)

import sys
import math

input = sys.stdin.readline().split()
T = int(input[0])
N = 0
mx = 0
my = 0
mz = 0
mvx = 0
mvy = 0
mvz = 0

def calcdist(t):
	global mx, my, mz, mvx, mvy, mvz
	px = mx + t * mvx
	py = my + t * mvy
	pz = mz + t * mvz
	return px * px + py * py + pz * pz

def findmin(lot, lod, hit, hid):
	#print "#", lot, lod, hit, hid
	midt = 0.5 * (lot + hit)
	midd = calcdist(midt)
	if hit - lot < 0.00000001:
		return midt
	elif lod <= hid:
		return findmin(lot, lod, midt, midd)
	else:
		return findmin(midt, midd, hit, hid)

SS = 20000

for t in xrange(T):
	input = sys.stdin.readline().split()
	N = int(input[0])
	mx = 0
	my = 0
	mz = 0
	mvx = 0
	mvy = 0
	mvz = 0
	for n in xrange(N):
		input = sys.stdin.readline().split()
		mx += int(input[0])
		my += int(input[1])
		mz += int(input[2])
		mvx += int(input[3])
		mvy += int(input[4])
		mvz += int(input[5])
	mx = mx * 1.0 / N
	my = my * 1.0 / N
	mz = mz * 1.0 / N
	mvx = mvx * 1.0 / N
	mvy = mvy * 1.0 / N
	mvz = mvz * 1.0 / N
	#print "#", mx, my, mz, mvx, mvy, mvz
	mint = findmin(0, calcdist(0), SS, calcdist(SS))
	mind = math.sqrt(calcdist(mint))
	print 'Case #%d: %.8f %.8f' % (t + 1, mind, mint)


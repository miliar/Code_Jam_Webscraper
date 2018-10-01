import math

class Circle:
	def __init__(self, x, y, r):
		self.x = x
		self.y = y
		self.r = r

	def stGetDistance2(c1, c2):
		return c1.r + c2.r + math.sqrt((c2.x-c1.x)**2 + (c2.y-c1.y)**2)

def getFar2(circles):
	n = len(circles)
	dmax = float(0)
	thetwo = [None, None]

	for i in range(n):
		c1 = circles[i]
		for j in range(n):
			c2 = circles[j]
			d = c1.r + c2.r + math.sqrt((c2.x-c1.x)**2 + (c2.y-c1.y)**2)
			if d > dmax:
				dmax = d
				thetwo[0] = c1
				thetwo[1] = c2
	return thetwo

def getMinRadius3(circles):
	thetwo = getFar2(circles)
	c1 = thetwo[0]
	c2 = thetwo[1]

	dmax = float(0)

	n = len(circles)
	for i in range(n):
		c = circles[i]
		d1 = c.r + c1.r + math.sqrt((c.x-c1.x)**2 + (c.y - c1.y)**2)
		d2 = c.r + c2.r + math.sqrt((c.x-c2.x)**2 + (c.y - c2.y)**2)
		d = min(d1, d2)
		if d > dmax:
			dmax = d

	return dmax/2

def getMinRadius(circles):
	n = len(circles)

	if n == 0:
		return 0
	elif n == 1:
		return circles[0].r
	elif n == 2:
		return max(circles[0].r, circles[1].r)
	else:
		return getMinRadius3(circles)

	
import sys

fileNamePrefix = sys.argv[1]
fileNameIn = fileNamePrefix + ".in"
fileNameOut = fileNamePrefix + ".out"

fileIn = open(fileNameIn, 'r')
lines = fileIn.readlines()

testcnt = int(lines[0])
idx = 1

fileOut = open(fileNameOut, 'w')

for test in range(testcnt):
	plantcnt = int(lines[idx])
	idx += 1

	circles = []
	for i in range(plantcnt):
		nums = [int(n) for n in lines[idx].strip().split(' ')]
		idx += 1
		#print nums[0], nums[1], nums[2]
		circles.append(Circle(nums[0], nums[1], nums[2]))

	res = getMinRadius(circles)
	print("Case #{0}: {1:.8f}".format(test + 1, res))
	fileOut.write("Case #{0}: {1:.8f}\n".format(test + 1, res))

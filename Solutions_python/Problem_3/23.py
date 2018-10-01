#!/usr/bin/env python

import math

INPUT_FILE = 'C-large.in'

def process(case, f, R, t, r, g):

	def get_hole(max_dist, x1, y1, g):

		def convex(convex_x, convex_y):
			convex_x.append(convex_x[0])
			convex_y.append(convex_y[0])
			
			total = 0.0
			for i in range(len(convex_x) - 1):
				total = total + convex_x[i] * convex_y[i + 1]
			for i in range(1, len(convex_x)):
				total = total - convex_x[i] * convex_y[i - 1]

			return total / 2.0

		dist1 = math.sqrt(x1 * x1 + y1 * y1)
		if dist1 >= max_dist:
			return 0.0

		x2 = x1 + g
		y2 = y1 + g
		dist2 = math.sqrt(x2 * x2 + y2 * y2)
		if dist2 < max_dist:
			return g * g

		# we know that (x1, y1) is in and (x2, y2) is not
		# now we have 4 cases
		# (x2, y1) is in or not = bool in1
		# (x1, y2) is in or not = bool in2

		dist = math.sqrt(x2 * x2 + y1 * y1)
		in1 = (dist < max_dist)
		dist = math.sqrt(x1 * x1 + y2 * y2)
		in2 = (dist < max_dist)
		#print '---'
		#print x1, y1, in1, in2
		#print g * g
		
		# and we'll get 2 intersection points (px1, py1), (px2, py2)
		px1 = 0.0
		py1 = 0.0
		px2 = 0.0
		py2 = 0.0

		if in1:
			# (px1, py1) is on (x2, y1) - (x2, y2)
			px1 = x2
			py1 = math.sqrt(max_dist * max_dist - px1 * px1)
		else:
			# (px1, py1) is on (x1, y1) - (x2, y1)
			py1 = y1
			px1 = math.sqrt(max_dist * max_dist - py1 * py1)

		if in2:
			# (px2, py2) is on (x1, y2) - (x2 - y2)
			py2 = y2
			px2 = math.sqrt(max_dist * max_dist - py2 * py2)
		else:
			# (px2, py2) is on (x1, y1) - (x1 - y2)
			px2 = x1
			py2 = math.sqrt(max_dist * max_dist - px2 * px2)

		# must be ccw
		convex_x = [x1]
		convex_y = [y1]

		if in1:
			convex_x.append(x2)
			convex_y.append(y1)

		convex_x.append(px1)
		convex_y.append(py1)

		convex_x.append(px2)
		convex_y.append(py2)
			
		if in2:
			convex_x.append(x1)
			convex_y.append(y2)

		convex_size = convex(convex_x, convex_y)

		# here, we add the curved part
		pie = max_dist * max_dist * (math.atan2(py2, px2) - math.atan2(py1, px1)) / 2.0
		triangle = convex([0, px1, px2], [0, py1, py2])

		return convex_size + pie - triangle

	# we assume the fly is a point
	r = r + f
	g = g - 2 * f
	t = t + f
	f = 0.0

	total_quadrant = math.pi * (R * R) / 4		# I'm intersted of only the first quadrant
	total_hole = 0.0

	if g >= 0.0:
		x = 0.0
		while x < R - t:
			y = 0.0
			while y < R - t:
				total_hole = total_hole + get_hole(R - t, x + r, y + r, g)
				y = y + g + 2 * r
			x = x + g + 2 * r

	print 'Case #%d: %f' % (case, (total_quadrant - total_hole) / total_quadrant)

fp = open(INPUT_FILE, 'r')

n = int(fp.readline())

for case in range(1, n + 1):
	f, R, t, r, g = map(float, fp.readline().split())
	process(case, f, R, t, r, g)

fp.close()

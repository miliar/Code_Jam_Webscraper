from math import pi, sin, asin, sqrt

def quad_area(r, a, b):
	abr = asin(b/r)
	aar = asin(a/r)
	return r * r * (2 * abr + sin(2*abr) - 2 * aar - sin(2*aar)) / 4

def main():
	n = int(raw_input())
	for num in range(n):
		f, R, t, r, g = map(float, raw_input().split(' '))
		if 0:
			print "f =", f
			print "R =", R
			print "t =", t
			print "r =", r
			print "g =", g
	
		# Pretend the fly is smaller and the strings are bigger
		# Same result; less variables
		t += f
		g -= 2 * f
		r += f
		Ri = R - t	# Radius of possible fly safe area

		if g <= 0:
			prob = 1
		else:
			# Find the total area of the gaps
			stride = g + 2 * r
			row = 0
			safe_area = 0
			complete_total = 0
			while True:
				bl_y = r + row * stride
				if bl_y > Ri:
					break
				tr_y = bl_y + g
				
				# How many complete (square) gaps on this row?
				# Find intersection of y = tr_y with inner rim
				if Ri > tr_y:
					rim_top_x = sqrt(Ri * Ri - tr_y * tr_y)
				else:
					rim_top_x = 0

				complete_this_row = int((rim_top_x + r) / stride)
				complete_total += complete_this_row

				rim_bottom_x = sqrt(Ri * Ri - bl_y * bl_y)

				# First column on this row which may intersect the inner rim
				column = complete_this_row
				while True:
					bl_x = column * stride + r
					if bl_x > rim_bottom_x:
						break
					tr_x = bl_x + g
					# (bl_x, bl_y), (tl_x, tl_y) is a square that intersects the inner rim
					
					if rim_top_x > bl_x:
						# Inner rim intersects the top of this box
						safe_area += (rim_top_x - bl_x) * g
						curve_min_x = rim_top_x
						assert rim_top_x < tr_x
					else:
						# Inner rim intersects the left side of this box
						curve_min_x = bl_x

					assert curve_min_x < tr_x

					curve_max_x = min(rim_bottom_x, tr_x)
					assert curve_max_x > curve_min_x
					area_under_curve = quad_area(Ri, curve_min_x, curve_max_x)
					area_under_curve -= (curve_max_x - curve_min_x) * bl_y
					assert area_under_curve > 0

					safe_area += area_under_curve
					column += 1
				row += 1
				
			safe_area += complete_total * g * g
			total_area = pi * R * R

			prob = 1 - (4 * safe_area / total_area)

		print "Case #%d: %.6f" % (num + 1, prob)

main()

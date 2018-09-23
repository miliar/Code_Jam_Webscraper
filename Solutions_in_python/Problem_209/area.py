import math as m
import operator


def radius_area(r):
	return m.pi * r * r

def height_area(h, r):
	return 2 * m.pi * r * h

def max_area(N, K, radius, height):

	listy = [(radius[i], height_area(height[i], radius[i])) for i in xrange(N)]

	max_result = -1

	for i in xrange(N):
		current_r = radius[i]
		current_h = height[i]

		partial_listy = filter(lambda x : x[0] <= current_r, listy)

		if len(partial_listy) < K:
			continue

		partial_listy.remove((current_r, height_area(current_h, current_r)))

		partial_listy_sorted = sorted(partial_listy, key=operator.itemgetter(1))
		partial_listy_sorted.reverse()

		# print partial_listy_sorted

		result = radius_area(current_r) + height_area(current_h, current_r) + sum([partial_listy_sorted[j][1] for j in xrange(K-1)])

		if result > max_result:
			max_result = result
			# print max_result

	return max_result

	# max_rad = max(radius)
	# indexes = filter(lambda x : x[1]==max_rad, enumerate(radius))

	# first_l = [(i, height[i]) for (i, r) in indexes]
	# first, max_h = max(first_l, key=operator.itemgetter(1))

	# to_del = height_area(max_h, max_rad)
	# result = radius_area(max_rad) + height_area(max_h, max_rad)

	# listy = [height_area(height[i], radius[i]) for i in xrange(N)]
	# listy.remove(to_del)
	# listy_s = sorted(listy)
	# listy_s.reverse()

	# result += sum(listy_s[:(K-1)])

	# return result


def main():
	T = int(raw_input())

	for t in xrange(T):

		line = raw_input().split()
		N, K = int(line[0]), int(line[1])

		radius = []
		height = []
		for p in xrange(N):
			line = raw_input().split()
			radius.append(int(line[0]))
			height.append(int(line[1]))

		print 'Case #'+str(t+1)+': '+str(max_area(N, K, radius, height))


main()
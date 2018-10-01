import sys
from collections import defaultdict

def calc(count, length, N):
	if length == 0:
		return 0
	val = length * N - (length * (length +1)/2) + length
	return val * count

if __name__ == '__main__':
	cases = int(sys.stdin.readline())

	for case in xrange(1, cases + 1):
		N, M = [int(val) for val in sys.stdin.readline().strip().split()]
		ends = defaultdict(lambda: defaultdict(lambda: 0))
		starts = defaultdict(lambda: 0)
		points = set()
		original = 0
		for i in xrange(M):
			start, end, count = [int(val) for val in sys.stdin.readline().strip().split()]
			original += calc(count, end - start, N)
			ends[end][start] += count
			starts[start] += count
			points.add(start)
			points.add(end)
		points = list(points)
		points.sort()

		for val in points:
			if val in ends:
				cur_starts = ends[val].keys()
				cur_starts.sort()
				for start in cur_starts:
					count = ends[val][start]
###					print ' ' * start + '.' * (val - start) + ' ' + str(count) + ' ' + str(val - start)

###		print "Edited"

		cur = []
		lengths = defaultdict(lambda: 0)
		for val in points:
			if val in starts:
				cur.append((val, starts[val]))
			if val in ends:
				cur_starts = ends[val].keys()
				cur_starts.sort()
				ended = 0
				used = 0
				for start in cur_starts:
					count = ends[val][start]
					ended += count
					while count > 0:
						available = cur.pop()
						if count < available[1]:
							lengths[val - available[0]] += count
							cur.append((available[0], available[1] - count))
							tstart = available[0]
###							print ' ' * tstart + '.' * (val - tstart) + ' ' + str(count) + ' ' + str(val - tstart)
							break
						else:
							lengths[val - available[0]] += available[1]
							count -= available[1]
							used += 1
							tstart = available[0]
							tcount = available[1]
###							print ' ' * tstart + '.' * (val - tstart) + ' ' + str(tcount) + ' ' + str(val - tstart)
		total = 0
		for length in lengths:
			total += calc(lengths[length], length, N)
		total = original - total
		print "Case #%d: %d" % (case, total % 1000002013)

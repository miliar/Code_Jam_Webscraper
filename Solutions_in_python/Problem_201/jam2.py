import math
import bisect
from sortedcontainers import SortedSet
from operator import itemgetter
from multiprocessing import Pool

def proc(x):
	case, n, k = [int(s) for s in x.split(" ")]
	sections = SortedSet(key=itemgetter(2, 3))
	sections.add((0, n + 1, n, n + 1))

	for i in range(n):
		section = sections.pop()

		half = math.floor((section[0] + section[1]) / 2)
		section1 = (section[0], half, half - section[0] - 1, n + 1 - section[0])
		section2 = (half, section[1], section[1] - half - 1, n + 1 - half)

		#print(i, half)

		if i + 1 == k:
			Ls = section1[2]
			Rs = section2[2]
			return (case, max(Ls, Rs), min(Ls, Rs))
			break

		if section1[2] > 0:
			sections.add(section1)

		if section2[2] > 0:
			sections.add(section2)

		#print(sections)

if __name__ == "__main__":
	t = int(input())

	lst = []
	for case in range(1, t + 1):
		lst.append(str(case) + " " + input())

	pool = Pool(12)
	lst2 = pool.map(proc, lst)

	for i in lst2:
		print("Case #%d: %d %d" % i)
		
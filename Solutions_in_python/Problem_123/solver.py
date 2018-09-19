import sys
import copy
import time
from collections import OrderedDict

answer = {};

def solve(c):

	armin = c[0]
	motes = c[1]
	moteIndex = 0

	if armin == 1:
		return len(motes)
	elif len(motes) == 0:
		return 0

	while True:
		for j in range(moteIndex, len(motes), 1):
			if motes[j] < armin:
				armin += motes[j]
				moteIndex += 1

		if moteIndex == len(motes):
			return 0
		

		tmpMote = copy.deepcopy(motes)
		tmpMote.append(armin-1)
		tmpMote.sort()
		solve1 = solve((copy.deepcopy(armin), tmpMote[moteIndex:]))


		solve2 = solve((copy.deepcopy(armin), copy.deepcopy(motes[moteIndex:-1])))

		if solve1 < solve2:
			return solve1 + 1
		else:
			return solve2 + 1
				

def prepare():
        lines = sys.stdin.readlines()
        nbCase = int(lines[0])
        case = {}
        for i in range(nbCase):
                split = lines[2*i+1].split(' ')
		armin = split[0]
		split = lines[2*i+2].split(' ')
		res = []
		for j in split:
			res.append(int(j))
		res.sort()
                case[i+1] = (int(armin), res)
        return case


if __name__ == "__main__":
	prep = prepare()
	res = {}
	for i in prep:
		res[i] = solve(prep[i])
	for i in res:
		print "Case #" + str(i) + ": " + str(res[i])

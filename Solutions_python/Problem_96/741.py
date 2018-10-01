#!/usr/bin/env python

def main():
	import sys

	sys.stdin.readline()
	casenum = 1
	while True:
		line = sys.stdin.readline().strip()
		if line=='': break
		raw0 = line.split(' ', 3)
		n, surprises, target, raw1 = int(raw0[0]), int(raw0[1]), int(raw0[2]), raw0[3]
		totals = map(int, raw1.split(' '))
		assert len(totals) == n
		
		nCanReachTargetNoSurprise = 0
		nCanReachTargetBySurprise = 0
		for total in totals:
			base = total // 3
			rem = total % 3

			baseScore = [base, base, base]
			normalScore = listAdd(baseScore, scoreAdds[rem][False])
			surprisingScore = listAdd(baseScore, scoreAdds[rem][True])
			# print normalScore, surprisingScore

			if isValid(normalScore) and  max(normalScore) >= target:
				nCanReachTargetNoSurprise += 1
				continue
			if isValid(surprisingScore) and max(surprisingScore) >= target: nCanReachTargetBySurprise += 1
			
		
		#print n, '-', totals
		print 'Case #%s:' % casenum, nCanReachTargetNoSurprise + min(surprises, nCanReachTargetBySurprise)
		casenum += 1


class InvalidScoreError(Exception): pass

def isValid(score):
	a = min(score); b = max(score)
	if not (b-a <= 2): return False
	if a < 0: return False
	return True

def listAdd(a, b): return map(lambda x,y:x+y, a, b)

scoreAdds = [
	{False: [0,0,0], True: [-1, 0, 1]},
	{False: [0,0,1], True: [-1, 1, 1]},
	{False: [0,1,1], True: [0, 0, 2]},
	]

if __name__ == '__main__': main()

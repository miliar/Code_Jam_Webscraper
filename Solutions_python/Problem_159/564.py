import math
def firstMethod(mush):
	
	ans = 0
	for i in xrange(0, len(mush) - 1):
		if mush[i+1] < mush[i]:
			ans += mush[i] - mush[i+1]
	return ans

def secondMethod(mush):
	maxDiff = -1
	for i in xrange(0, len(mush) -1):
		if mush[i+1] < mush[i]:
			cand = mush[i] - mush[i+1]
			maxDiff = max(maxDiff, cand)
	ans = 0
	if maxDiff == -1: return ans
	for i in mush[:-1]:
		if i < maxDiff:
			ans += i
		else:
			ans += maxDiff
			
	return ans

f = open("A-large.in", 'r')
f2 = open("outputMushLarge.txt", 'w')	
t = int(f.readline())
for i in xrange(t):
	s = "Case #" + str(i+1) + ": "
	numMush = int(f.readline())
	mush = map(int, f.readline().split())
	if i == t-1:
		f2.write(s+str(firstMethod(mush)) + ' ' + str(secondMethod(mush)))
	else:
		f2.write(s+str(firstMethod(mush)) + ' ' + str(secondMethod(mush)) + '\n')
f.close()
f2.close()
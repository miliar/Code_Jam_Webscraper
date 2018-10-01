import math

def adjustStalls(stalls, length, pos):
	offset = int(math.floor(length / 2))

	if length % 2 == 0:
		offset -= 1

	if stalls[pos + offset] == 1:
		print "ERROR"
	stalls[pos + offset] = 1
	return (stalls, pos + offset)

def getLargestSpace(stalls):
	largest = (0,None)
	cur = (0,0)
	for i in range(len(stalls)):
		stall = stalls[i]
		if stall == 1:
			cur = (0,i+1)
			#print 'skipping at index '+ str(i)
		else:
			cur = (cur[0]+1, cur[1])
			if cur[0] > largest[0]:
				largest = cur
				#print 'updating largest: '+ str(largest)
	return largest #(lengh, pos)


def getMinMaxA(stalls, pos):
	
	before = 0
	posb = pos - 1
	while posb >= 0 and stalls[posb] == 0:
		before += 1
		posb -= 1

	after = 0
	posa= pos + 1
	while posa < len(stalls) and stalls[posa] == 0:
		after += 1
		posa += 1

	# print stalls, pos
	# print before, after
	return (max(before, after), min(before, after))

C = int(raw_input())
# C = 1
for i in range(C):

	inputs = [int(x) for x in raw_input().split(' ')]
	N = inputs[0]
	K = inputs[1]


	stalls = [1] + ([0] * N) + [1]
	for j in range(K):
		
		(length, pos) = getLargestSpace(stalls)
		(stalls, pos) = adjustStalls(stalls, length, pos)
	
	(maxF, minF) = getMinMaxA(stalls, pos)
	
	print 'Case #%d: %d %d' % (i+1, maxF, minF)
	

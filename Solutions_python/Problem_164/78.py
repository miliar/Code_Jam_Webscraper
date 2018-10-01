import math
infile = open('C-small-2-attempt2.in', 'r')
outfile = open('out.txt.', 'w')

def GetKey(i):
	return i[2]

def CheckPass(i, j):
	dj = j[0]
	mj = j[1]

	ti = i[2]
	tj = mj - ((dj * mj)/float(360))

	if tj >= ti:
		return 0

	return math.floor((ti - tj)/mj)

t = int(infile.readline().strip())

for case in xrange(t):
	n = int(infile.readline().strip())
	groups = []
	for i in xrange(n):
		groups.append([int(j) for j in infile.readline().strip().split()])
	
	
	# solve problem
	hikers = []
	for i in groups:
		for j in xrange(i[1]):
			d, h, m = [float(x) for x in i]
			hikers.append((d, m+float(j),((m+float(j))-((d*(m+float(j)))/(float(360))))))

	hikers = sorted(hikers, key=GetKey, reverse=True)

	# find ans
	ans = 0
	best = [1000000]

	while ans <= len(hikers):
		if ans == len(hikers):
			break
		if ans > 0:
			if hikers[ans][2] == hikers[ans-1][2]:
				ans += 1
				continue
		count = 0
		for j in hikers[ans+1:] + hikers[0:ans]:
			count += CheckPass(hikers[ans], j)
		
		if count == 0:
			break
		#elif (ans + count) > lastans:
		#	ans = lastans
		#	break
		#lastans = ans+count
		best.append(ans + int(count))

		ans += 1
	#ans = min(best)

	outfile.write('Case #%d: %d\n' % (case+1, min(ans, min(best)) ))

infile.close()
outfile.close()

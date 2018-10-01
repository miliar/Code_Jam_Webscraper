from fractions import Fraction
def solve():
	played = []
	wps = []
	owps = []
	oowps = []
	for i in xrange(N):
		play = 0
		wins = 0
		for char in games[i]:
			play += 1 if char != '.' else 0
			wins += 1 if char == '1' else 0
		played.append(play)
		wps.append(Fraction(wins, play))
	for i in xrange(N):
		owp = 0
		count = 0
		for idx, char in enumerate(games[i]):
			if idx == i : continue
			if char != '.':
				cur = ((wps[idx] * played[idx]) - (0 if char == '1' else 1)) / (played[idx] - 1)
#				print "idx = %s :(%s * %s - %s) / %s = %s" % (idx, wps[idx], played[idx], 0 if char == '1' else 1, played[idx] - 1, cur)
				owp += cur 
#				print owp
				count += 1
#		print "i = %s : owp = %s, count = %s" % (i, owp, count)
		owps.append(owp / count)
	for i in xrange(N):
		oowp = 0
		count = 0
		for idx, char in enumerate(games[i]):
			if idx == i : continue
			if char != '.':
				oowp += owps[idx]
				count += 1
		oowps.append(oowp / count)
#	print [(wps[i], owps[i], oowps[i]) for i in xrange(N)]
	return [str(0.25 * float(wps[i]) + 0.5 * float(owps[i]) + 0.25 * float(oowps[i])) for i in xrange(N)]
	
T = int(raw_input())
for case in xrange(1, T + 1):
	N = int(raw_input())
	games = [raw_input().strip() for i in xrange(N)]
	ans = solve()
	print "Case #%d:\r\n%s" % (case, "\r\n".join(ans))
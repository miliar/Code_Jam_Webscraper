def CalculateCookies():
	input = raw_input().split(' ')
	
	c = float(input[0])
	f = float(input[1])
	x = float(input[2])

	nTimeToFarm = [0]
	nTimeToCookies = [x / 2.0]

	i = 1
	while True:
		nCookiesPerSec = 2 + (i - 1) * f
		nCookiesPerSecAfterFarm = 2 + i * f

		nTimeToFarm += [nTimeToFarm[-1] + (c / nCookiesPerSec)]
		nTimeToCookies += [nTimeToFarm[i] + (x / nCookiesPerSecAfterFarm)]
		
		if (len(nTimeToCookies) > 1) and (nTimeToCookies[-1] > nTimeToCookies[-2]):
			return nTimeToCookies[-2]
		i += 1
			
nCases = int(raw_input())
for nCase in xrange(nCases):
	print "Case #%d: %.7f" %(nCase + 1, CalculateCookies())

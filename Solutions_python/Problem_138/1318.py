# Solution to "Deceitful War" for Google Code Jam 2014
# by Peter Mattsson (quantum.caffeine@gmail.com)
import sys

def inputData():
	with open(sys.argv[1], 'r') as infile:
		numCases = int(infile.readline())
		for c in range(numCases):
			n = int(infile.readline())
			blocks = [[float(x) for x in infile.readline().split()] for _ in range(2)]
			yield (n, blocks)


outfile = open(sys.argv[2], 'w')

for case,(n,(naomio,keno)) in enumerate(inputData()):
	naomio.sort()
	keno.sort()
	# Play Deceitful War
	naomi = list(naomio)
	ken = list(keno)
	dScore = 0
	while len(naomi) > 0:
		if naomi[-1] > ken[-1]:
			naomi.pop()
			ken.pop()
			dScore += 1
		else:
			naomi.pop(0)
			ken.pop()
	# Play War
	naomi = list(naomio)
	ken = list(keno)
	wScore = 0
	for block in reversed(naomi):
		if block > ken[-1]:
			ken.pop(0)
			wScore += 1
		else:
			pos = len(ken)-1
			while ken[pos] > block:
				pos -= 1
				if pos < 0:
					break
			pos += 1
			ken.pop(pos)
	outfile.write("Case #%d: %d %d\n"%(case+1, dScore, wScore))

outfile.close()
inf = open('a-large.in', 'r')
outf = open('LightAns.txt', 'w')

T = int (inf.readline())
for i in xrange(T):
	c = inf.readline()
	c = map(int, c.split())
	N = c[0]
	K = c[1]
	light = True
	for j in xrange(N):
		all = K/(2**j)
		if all%2 == 0:			
			light = False
			break
	if light == True:
		outf.write ('Case #' + str(i+1) + ': ' + 'ON' + '\n')
	else:
		outf.write ('Case #' + str(i+1) + ': ' + 'OFF' + '\n')

inf.close()
outf.close()


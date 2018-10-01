import sys

f = open(sys.argv[1], "r")
T = int(f.readline())

for c in range(T):
	i = map(float,f.readline().split())
	N = i[0]
	i = i[1:]
	s = sum(i)
	ta = 2*s/N

	lt = [k for k in i if k<ta]
	score = (s+sum(lt))/len(lt)
	tmp = []
	
	for k in i:
		tmp.append(100*max(0, score-k)/s)
	print "Case #" + str(c+1) + ": " + " ".join(map(str,tmp))	

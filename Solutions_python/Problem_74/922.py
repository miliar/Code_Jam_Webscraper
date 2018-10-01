import sys

def solve(line,case):
	time = otime = btime = 0
	opos = bpos = 1
	for i in range(0,len(line)-1,2):
		bot, pos = line[i],int(line[i+1])
		if bot == 'O':
			reqtime = pos-opos if pos>opos else opos-pos
			timediff = time - otime
			reqtime = reqtime - timediff if reqtime>timediff else 0
			time = otime = time + reqtime + 1
			opos = pos
		elif bot == 'B':
			reqtime = pos-bpos if pos>bpos else bpos-pos
			timediff = time - btime
			reqtime = reqtime - timediff if reqtime>timediff else 0
			time = btime = time + reqtime + 1
			bpos = pos
	print "Case #%s: %s" % (case, time)

with open(sys.argv[1]) as fp:
	cases = int(fp.readline())
	for i in range(1,cases+1):
		solve(fp.readline().strip().split()[1:],i)

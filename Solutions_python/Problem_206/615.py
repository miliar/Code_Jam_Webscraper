import sys, math

sys.setrecursionlimit(2500)

from collections import Counter

inp = open("in.txt")
#out = sys.stdout
out = open("out.txt","w+")

IMP = "IMPOSSIBLE"

def print_case(case, result):
    debug("Case #%d: %s" % (case, str(result)))
    out.write("Case #%d: %s\n" % (case, str(result)))

def debug(message):
	if len(sys.argv) > 1 and sys.argv[1] == "silent":
		return
	sys.stdout = sys.__stdout__
	print message
	sys.stdout = out

def read_ints(f=False):
    g =float if f else int
    return [g(x) for x in inp.readline().split()]

T = int(inp.readline())
for t in xrange(T):
    d, n = read_ints()
    d = float(d)
    
    horses = []
    for i in xrange(n):
        horses.append(read_ints(f=True))
    
    horses.sort(reverse=True)
    
    arrival_time = -1
    for horse in horses:
        position, speed = horse
        dist = d - position
        arv = dist / speed
        arrival_time = max(arrival_time, arv)
    
    s = d / arrival_time
    print_case(t+1, s)

import sys, math

sys.setrecursionlimit(2500)

from collections import Counter

inp = open("in.txt")
#inp = sys.stdin
out = open("out.txt","w+")

def print_case(case, result):
    debug("Case #%d: %s" % (case, str(result)))
    out.write("Case #%d: %s\n" % (case, str(result)))

def debug(message):
	if len(sys.argv) > 1 and sys.argv[1] == "silent":
		return
	sys.stdout = sys.__stdout__
	print message
	sys.stdout = out


def get_distances(stalls):
    l = 0
    r = 0
    distances = [[0, 0] for i in xrange(len(stalls))]
    for i in xrange(len(stalls)):
        distances[i][0] = l
        distances[-(i+1)][1] = r
        if stalls[i]:
            l = -1
        if stalls[-(i+1)]:
            r = -1
        
        l += 1
        r += 1
    
    return distances 


def get_fill_index(stalls):
    distances = get_distances(stalls)
    key = lambda i: (-min(distances[i]),-max(distances[i]), -i)
    options = sorted([i for i in range(len(stalls)) if not stalls[i]], key=key)
    chosen = options[0]
    return [chosen] + distances[chosen]
    

T = int(inp.readline())

for t in xrange(T):
    n, k = [int(x) for x in inp.readline().split()]
    stalls = [False] * n
    for i in xrange(k):
        fill_index, d1, d2 = get_fill_index(stalls)
        stalls[fill_index] = True
    
    print_case(t + 1, "%s %s" % (max(d1, d2), min(d1, d2)))
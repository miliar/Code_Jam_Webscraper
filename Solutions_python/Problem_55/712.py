import sys

def parse(f):
        for line in f:
                yield line.rstrip('\n').split(" ")

def process(a, R, k, groups):
	money = 0
	offset = 0
	for i in range(R):
		ride = 0
		gr = 0
		while(ride + groups[offset%len(groups)] <= k and gr < len(groups)):
			ride += groups[offset%len(groups)]
			money += groups[offset%len(groups)]
			offset += 1
			gr += 1
	print ("Case #%i: %i") % (a, money)
			
			

f = open(sys.argv[1])
nb = f.readline().rstrip('\n').split(" ")[0]
a = 1
for i in range(int(nb)):
	rkn = f.readline().rstrip('\n').split(" ")
	R = rkn[0]
	k = rkn[1]
	
	groups = f.readline().rstrip('\n').split(" ")
	groups = map(int, groups)
	process(a, int(R), int(k), groups)
	a += 1

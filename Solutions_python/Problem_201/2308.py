import math
filein = open('C-small-2-attempt0.in', 'r')
fileout = open('C-small-2-attempt0.out', 'w')
 
T = int(filein.readline())
for t in range(T):
    fileout.write('Case #%d: ' % (t + 1))
    inp = [int(x) for x in filein.readline().split()]
    lvl = math.floor(math.log(inp[1], 2))
    offset = inp[1] - math.pow(2, lvl) + 1
    c1 = int(inp[0]/math.pow(2, lvl))
    s = inp[0] - math.pow(2, lvl) + 1
    u = c1 if s - (c1-1) * math.pow(2, lvl) >= offset else c1 - 1
    u = u*1.0
    # for tt in range(TT*2-1):
    # 	inp.append()
    
    # result = []

    # for i in range(TT):
    # 	seen = []
    # 	for j in range(TT*2-1):
    # 		seen.append(inp[j][i])
    # 	val = sorted(seen)[2*i]
    # 	# print seen
    # 	# print val

    # 	candidates = []
    # 	for j in range(TT*2-1):
    # 		if inp[j][i] == val:
    # 			candidates.append(inp[j])
    # 	if len(candidates) == 1:
    # 		seen.append(val)
    # 		# print candidates
    # 		# print seen
    # 		for x in candidates[0]:
    # 			seen.remove(x)
    # 		result = sorted(seen)
    # for u in result:

    fileout.write(str(int(math.ceil((u-1)/2)))+" "+ str(max(0, int(math.floor((u-1)/2)))))
    fileout.write("\n")		

    
 
filein.close()
fileout.close()
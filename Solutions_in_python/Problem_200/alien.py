import math
filein = open('B-large.in', 'r')
fileout = open('B-large.out', 'w')
 
T = int(filein.readline())
for t in range(T):
    fileout.write('Case #%d: ' % (t + 1))
    # inp = [int(x) for x in filein.readline().split()]
    inp = [int(x) for x in filein.readline().strip()]
    ans = []
    for i in range(len(inp)):
    	for j in range(10)[::-1]:
	    	if ans + [j]*(len(inp)-i) <= inp:
	    		ans = ans + [j]
	    		break
	    	


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

    fileout.write(str(int(''.join(map(str,ans)))))
    fileout.write("\n")		

    
 
filein.close()
fileout.close()
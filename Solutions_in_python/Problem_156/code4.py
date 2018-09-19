import math
num = raw_input()
num = int(num)

for x in range(num):
    output = "Case #"+str(x+1)+': '
    i = raw_input()
    lis= raw_input().split()
    for i in range(len(lis)):
    	lis[i] = int(lis[i])
    
    m = max(lis)
    o = 999999
    for sq in range(1,m+1):
    	s = 0
        for x in lis:
        	s += int(x/sq)
        	if (x %sq == 0):
        		s-=1
        s += sq
        o = min(o,s)
    print output+str(o)
    		
    	
###
#
###

import math 

# first step : get input

n = raw_input()
T = []
for i in range(int(n)): T.append(raw_input().split())
	
# Second step : eval test

def output(state,i):
	print("Case #"+str(i)+": "+state)
	
i = 0
OFF,ON = "OFF","ON"

for test in T:
	i += 1 
	N = int(test[0])
	K = int(test[1])
	cycle = int(math.pow(2,N))
	if (K != 0 and (((K+1) % cycle) == 0)) : output(ON,i)
	else : output(OFF,i)


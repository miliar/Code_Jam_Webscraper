#
#  .py
#  
#
#  Created by FEI LIU on -/-/10.
#  Copyright (c) 2010 ucla. All rights reserved.
#

def r2(inList, N):
	i = 0
	rst = 0
	while(i<N):
		tmps = inList[i].split(' ')
		xi = int(tmps[0])
		yi = int(tmps[1])
		j = i
		while(j<N):
			parts = inList[j].split(' ')
			xj = int(parts[0])
			yj = int(parts[1]) 
			if((xi > xj) and (yi < yj)):
				rst += 1	
			if((xi < xj) and (yi > yj)):
				rst += 1
				print rst
			j += 1
		i += 1
	return rst



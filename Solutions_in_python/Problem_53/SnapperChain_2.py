#
#  SnapperChain.py
#  
#
#  Created by FEI LIU on 5/8/10.
#  Copyright (c) 2010 ucla. All rights reserved.
#

def snapperChain(nSnappers, kTimes):
	if(kTimes <= 0):
		return 0
	if(nSnappers <= 0):
		return 0
	
	m = nSnappers

	total = 1
	while(m>0):
		total *= 2 
		m = m -1
	
	snapperCount = total -1
	if((kTimes-snapperCount)%(snapperCount+1) == 0):
		return 1
	else:
		return 0
		


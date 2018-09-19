#
#  rd1.py
#  
#
#  Created by FEI LIU on -/-/10.
#  Copyright (c) 2010 ucla. All rights reserved.
#

def ffit(newDirList, nSize, oldDirList, oSize):
	i=0
	DHash = {}
	DHash['/'] = 1
	while(i<oSize):
		parts = oldDirList[i].split('/')
		j = 0
		temp = ''
		#don't add /?
		while(j<len(parts)):
			temp = temp + '/' + parts[j]
			if(not DHash.has_key(temp)):
				DHash[temp] = 1
			j += 1
		i += 1
	
	#judge the newDirList
	i = 0
	mkNo = 0
	while(i<nSize):
		parts = newDirList[i].split('/')
		j = 0
		temp = ''
		while(j<len(parts)):
			temp = temp + '/' + parts[j]
			if(not DHash.has_key(temp)):
				DHash[temp] = 1
				mkNo += 1
			j += 1
		i += 1
	
	return mkNo


	

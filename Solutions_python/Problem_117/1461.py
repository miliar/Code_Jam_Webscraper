'''

	Case #1: YES
	Case #2: NO
	Case #3: YES
    

'''


import os
import sys
import pdb
from os.path import basename

lmw_matrix = []
last_index = 1

def getResult(fo, mlist, index):	
	global lmw_matrix, last_index
	#pdb.set_trace()
	x = mlist[last_index].split()
	n = int(x[0])
	m = int(x[1])
	if n < 1 or n > 10 or m < 1 or m > 10:		
		print "Data input error"
		return
	s = last_index+1
	e = last_index+n
	last_index=e+1	
	 
	for i in range(s,e+1):
		lmw_matrix.append(mlist[i].split())		
	
	temp = [['100' for j in range(m)] for i in range(n)]	
	
	# sweep through rows
	for i in range(n):
		for j in range(m):
			if int(lmw_matrix[i][j]) > 2 or int(lmw_matrix[i][j]) < 1:
				print "Data input error"
				return
			temp[i][j] = max(lmw_matrix[i])
	
	#sweep through columns	
	for i in range(m):
		col = []
		max_col = '100'
		for j in range(n):
			col.append(lmw_matrix[j][i])
		max_col = max(col)
		for j in range(n):
			if temp[j][i]>max_col:
				temp[j][i] = max_col
			
		
	'''
	print "Printing matrix#: "+str(index)
	print lmw_matrix
	print "Printing temp matrix#: "+str(index)
	print temp
	'''
	
	s1 = set([tuple(lst1) for lst1 in lmw_matrix])
	s2 = set([tuple(lst2) for lst2 in temp])
	
	l = len(s1.symmetric_difference(s2))
	if l > 0:
		fo.write("Case #"+str(index)+": NO\n")
	elif l == 0:
		fo.write("Case #"+str(index)+": YES\n")
			
	return


if __name__ == "__main__":
	if len(sys.argv) != 2:
		sys.exit()
	
with open(sys.argv[1], 'r') as f:
	read_data = f.readlines()	

fo = open(os.path.splitext(basename(sys.argv[1]))[0]+".out", 'w')
# Extract test_case
test_case = int(read_data[0])


if test_case > 100 or test_case < 1:
	sys.exit()

#print read_data
#pdb.set_trace()
for i in range(test_case):
	lmw_matrix = []
	getResult(fo,read_data, i+1)
	

f.close()
fo.close()
	
	




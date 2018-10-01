import sys
import numpy as np
with open(sys.argv[1]) as f:
	content = f.readlines()
testcases = int(content[0].replace('\n',''))
print testcases
counter = 1
f=open('outfile','w')
for i in range(testcases):
	#counter = counter+1
	chooseOne = int(content[counter].replace('\n',''))
	counter1 = counter + chooseOne
	row1 = content[counter1].replace('\n','').split(' ')
	row1 = [int(s) for s in row1]
	counter = counter + 5
	choose2 = int(content[counter].replace('\n',''))
	counter2 = counter + choose2
	row2 = content[counter2].replace('\n','').split(' ')
	row2 = [int(s) for s in row2]
	r1 = set(row1)
	r2 = set(row2)
	result = r1.intersection(r2)
	counter = counter + 5	
	if len(result) == 1:
		f.write('Case #'+str(i+1)+': '+str(result.pop())+'\n')
		continue
	if len(result) > 1:
		f.write('Case #'+str(i+1)+': Bad magician!\n')
		continue
	if len(result) == 0:
		f.write('Case #'+str(i+1)+': Volunteer cheated!\n')
		continue
	
	
	
	
	


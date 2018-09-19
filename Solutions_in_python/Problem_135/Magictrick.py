import sys
import math
with open(sys.argv[1],"r") as f:
	content = f.readlines()
total = int(content[0])
counter =1
for i in range(1,total*10,10):
	firstList = []
	secondList = []
	first= int(content[i])
	second=int(content[i+5])
	for j in range(i+1,i+5):
		splitList = content[j].split()
		for item in splitList:
			firstList.append(item)
	for k in range(i+6,i+10):
		splitList = content[k].split()
		for item in splitList:
			secondList.append(item)
	firstList = firstList[(first-1)*4:(first*4)]
	secondList = secondList[(second-1)*4:second*4]
	common = set(firstList) & set(secondList)
	length =  len(common)
	print length
	with open("out.txt","a") as fout:
		if length ==1:
			element = common.pop()
			print "Case #"+str(counter)+":"+str(element)
			fout.write("Case #"+str(counter)+": "+str(element)+"\n")
			fout.close()
			counter=counter+1
		elif length>1:
			print "Case #"+str(counter)+": Bad magician!"
			fout.write("Case #"+str(counter)+": Bad magician! \n")
			fout.close()
			counter = counter+1
		else:
			print "Case #"+str(counter)+": Volunteer cheated"
			fout.write("Case #"+str(counter)+": Volunteer cheated! \n")
			fout.close()
			counter = counter+1

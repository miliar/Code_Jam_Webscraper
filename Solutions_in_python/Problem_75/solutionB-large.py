import collections
import string

infilename = "B-large.in"
outfilename = "B-large.out"

f = open(infilename,"r")
o = open(outfilename,"w")

noCases = int(f.readline())

for case in range(1,noCases+ 1):
	data = (f.readline()).split(" ")
	combine = {}
	oppose = []
	elementslist = []
	index = 0	
	idx = 0

	num = int(data[index])
	index = index + 1

	while (len(combine)< num):
		tmp = str(data[index])
		combine[str(tmp[0]+tmp[1])] = tmp[2]
		index = index + 1
	
	num = int(data[index])
	index = index + 1
	while (len(oppose)< num):
		tmp = str(data[index])
		oppose.append(tmp)
		index = index + 1

	num = int(data[index])
	index = index + 1
	elements = data[index]


	while(idx<len(elements)-1):
		elementpair= ""
		if(len(elementslist)>0):
			tmp = elementslist.pop()
			elementpair =  tmp +elements[idx]
		 
			if (elementpair in combine):
				elementslist.append(combine[elementpair])
			
			elif (elementpair[::-1] in combine):		
				elementslist.append(combine[elementpair[::-1]])
			else:
				elementslist.append(tmp)
				
				for e in elementslist:
					tmp = e + elements[idx]
					if (tmp in oppose):
						elementslist =[]
						break
					if (tmp[::-1] in oppose):
						elementslist =[]
						break

				if(len(elementslist)>0):
					elementslist.append(elements[idx])	
		else:
			elementslist.append(elements[idx])		
		idx = idx + 1
	
	data = ", ".join(elementslist)
		
	o.write( "Case #"+str(case)+": ["+data+"]\n")

f.close()
o.close()


if __name__=="__main__":
	iFile = open('G:/usaco/B-large.in', 'r')
	oFile = open('G:/usaco/B-large.out', 'w')
	caseNum = (int)(iFile.readline())
	for i in range(0, caseNum):
		text = iFile.readline().strip('\n').strip('\r')
		text = text.split(" ")
		out = "Case #"+str(i+1)+": "
		data = []
		m = 0
		for j in range(0, len(text)):
			data.append((int)(text[j]))
		numOfGooglers = data[0]
		surpriseNum = data[1]
		p = data[2]
		scores = data[3:]
		# get m
		for k in scores:
			comp = 3*p
			# print(k)
			if k>comp:
				m=m+1
			else:
				if k>=comp-2:
					m = m+1
				else:
					if (k>=comp-4) and (comp-4>0) and (surpriseNum>0):
						m = m+1
						surpriseNum = surpriseNum - 1
					
		out = out+str(m)+'\n'
		print(out)
		oFile.write(out)
	iFile.close()
	oFile.close()
	

# file: 1.py

import sys

testCasesQtd = input()
count = 0
for i in range(testCasesQtd):
	count = count + 1
	dataset = []
	testCaseTerms = raw_input().split(' ')
	cPos = 0
	dPos = (cPos + 1) + int(testCaseTerms[cPos])
	nPos = (dPos + 1) + int(testCaseTerms[dPos])
	
	cList = []
	for i in range(int(testCaseTerms[cPos])):
		cList.append(testCaseTerms[cPos+1+i])
	
	dList = []
	for i in range(int(testCaseTerms[dPos])):
		dList.append(testCaseTerms[dPos+1+i])
	
	nValues = testCaseTerms[nPos + 1]
	
	for value in nValues:
		if len(dataset) > 0:
			combined = False
			combinedItem = (value + dataset[len(dataset)-1])
			combinedItemReversedItem = (dataset[len(dataset)-1] + value)
			for item in cList:
				if (item[0:2] == combinedItem) or (item[0:2] == combinedItemReversedItem):
					dataset[len(dataset)-1] = item[2]
					combined = True
					break
						
			if not combined:			
				opposed = False
				for datasetItem in dataset:
					combinedItem = value + datasetItem
					combinedItemReversedItem = datasetItem + value
					for item in dList:
						if (combinedItem == item) or (combinedItemReversedItem == item):
							dataset = []
							opposed = True
							break
			if not combined and not opposed:
				dataset.append(value)
		else:
			dataset.append(value)
	
	print "Case #" + str(count) + ": " + str(dataset).replace("'","")
	
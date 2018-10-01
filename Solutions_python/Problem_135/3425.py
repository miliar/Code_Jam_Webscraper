import sys

lines = sys.stdin.readlines()

lineReader = 0
rowNums = list()
rowNums2 = list()
for testNum in range(int(lines[0])):
	ans = "0"
	badFlag = False
	startRow = testNum * 10 + 1
	targetOffset = int(lines[startRow])
	rowNums = lines[startRow + targetOffset].split(' ')

	rowNums[3] = rowNums[3].strip()	

	startRow += 5
	targetOffset = int(lines[startRow])
	rowNums2 = lines[startRow+targetOffset].split(' ')
	for i in range(4):
		temp = rowNums2[i].strip()
		for j in range(4):
			if temp == rowNums[j]:
				if ans == "0":
					ans = temp
				else:
					badFlag = True
	if badFlag:
		print "Case #%s: Bad Magician!" % (testNum + 1)
		continue
	if ans == "0":
		print "Case #%s: Volunteer cheated!" % (testNum + 1)
	else:
		print "Case #%s: %s" % (testNum + 1, ans)	
	

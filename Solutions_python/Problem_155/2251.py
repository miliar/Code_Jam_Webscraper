#!/usr/local/bin/python


def process(inputStr):
	standPpl = 0
	needPpl = 0
	for sidx, i in enumerate(inputStr):
		if i=="\n":
			continue
		needCurrent = 0
		if standPpl < sidx:
			needCurrent = sidx - standPpl
		standPpl += int(i) + needCurrent
		needPpl += needCurrent
	return str(needPpl)


fin = open('test.txt', 'r')
fout = open('result.txt', 'w')
line = fin.readline()
line = fin.readline()
caseNo = 1
while line:
	res = process(line.split(" ")[1])
	res = 'Case #' + str(caseNo) + ': ' + res + '\n'
	caseNo += 1
	fout.write(res)
	line = fin.readline()

fin.close();
fout.close();

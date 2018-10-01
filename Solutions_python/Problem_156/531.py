#!/usr/bin/env python
#encoding: utf-8

#case字符串　数值转换
def paseCase(caseLine):
	caseLine = caseLine.strip().split(' ');
	result = [int(elem) for elem in caseLine];
	result.sort();
	return result;

#计算num分钟吃完需要移动的最少次数
def step(caseList, num):
	count = 0;
	for elem in caseList:
		if(elem%num != 0):
			elem += num;
		count += elem/num - 1;
	return count;

def minMinutes(persons, caseLine):
	caseList = paseCase(caseLine);
	eatMinutes = 2;
	maxMinutes = caseList[-1];
	while eatMinutes < maxMinutes:
		moveMinutes = step(caseList, eatMinutes);
		if(moveMinutes + eatMinutes < maxMinutes):
			maxMinutes = moveMinutes + eatMinutes;
		eatMinutes += 1;
	return maxMinutes;

def run(inputFile, outputFile):
        fp = open(inputFile, 'r');
        fw = open(outputFile, 'w');

	caseCount = int(fp.readline());
	caseIndex = 0;
	while caseIndex < caseCount:
		caseIndex += 1;
		persons = int(fp.readline());
		string  = fp.readline();
		minutes = minMinutes(persons, string);
		fw.write("Case #%d: %d\n"%(caseIndex, minutes));

        fp.close();
        fw.close();

if __name__ == "__main__":
	run("in", "out");

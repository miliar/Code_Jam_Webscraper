#!/usr/bin/env python
#encoding: utf-8


def parseCase(line):
	line = line.strip();
	Smax = int(line[0]);
	audiences = line[-(Smax+1):];
	return Smax, audiences;


def minAudience(caseLine):
	Smax, audiences = parseCase(caseLine);
	index = 0;
	minCount = 0;
	audienceCount = 0;
	while(index <= Smax):
		if(audienceCount < index):
			minCount += 1;
			audienceCount += 1;
		audienceCount += int(audiences[index]);
		index += 1;
	return minCount;


def run(inputFile, outputFile):
	fp = open(inputFile, 'r');
	fw = open(outputFile, 'w');
	caseIndex = 0;
	count = -1;
	for line in fp:
		if(caseIndex == 0):
			count = int(line);
			caseIndex += 1;
		else:
			fw.write("Case #%d: %d\n"%(caseIndex, minAudience(line)));
			caseIndex += 1;
			count -= 1;
		if (count == 0):
			break;
	fp.close();
	fw.close();

if __name__ == "__main__":
	run("in", "out");

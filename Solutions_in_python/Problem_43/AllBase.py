import os
import sys
import logging

logger = logging.getLogger('MinimumScalarPrdt')
logger.setLevel(logging.INFO)
# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
# create formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
# add formatter to ch
ch.setFormatter(formatter)
# add ch to logger
logger.addHandler(ch)


def baseNToDec(baseN, number):
	decNumber = 0
	placingPosition = 1
	numberStr = str(number)
	for placing in numberStr:
		currentWeight = baseN**(len(numberStr) -placingPosition)
		digit = int(placing)
		decNumber +=digit* currentWeight
		placingPosition +=1
		
	return decNumber

def getMinBase(number):
	base =set()
	for i in number:
		base.add(i)
	if len(base)!=1:
		return len(base)
	else:
		return 2

def getMinNumber(base, number):
	numList = range(base)
	dict={}
	count =0
	ans=''
	while count < len(number):
		if count==0:
			num = str(numList.pop(1))
			dict[number[count]]=num
		else:
			if dict.has_key(number[count]):
				num = dict[number[count]]
			else:
				num = str(numList.pop(0))
				dict[number[count]]=num
		ans+=num
		count+=1
	return ans
	

def solve(input , output):
	numberOfTestCases = int(input.readline().strip())
	for i in range(numberOfTestCases):
		number = input.readline().strip()
		minBase = getMinBase(number)
		ans = baseNToDec(minBase, getMinNumber(minBase, number))
		output.write('Case #%i: %i \n' %(i+1, ans))

def main():
	input = open(sys.argv[1], 'r')
	output = open(sys.argv[2], 'w')
	solve(input, output)
	input.close()
	output.close()



if __name__=='__main__':
	main()

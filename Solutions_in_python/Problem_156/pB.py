from copy import deepcopy

def doNothing(diners):
	for i in range(len(diners)):
		if diners[i] > 0:
			diners[i] -= 1
	return diners


def specialMinutes(diners):
	pancakes = diners[diners.index(max(diners))]
	diners.append(pancakes // 2)
	diners[diners.index(max(diners))] -= pancakes // 2
	return diners


def specialMinutes9(diners):
	pancakes = diners[diners.index(9)]
	diners.append(6)
	diners[diners.index(max(diners))] = 3
	return diners


def secondMax(diners):
	d = deepcopy(diners)
	m = max(d)
	while max(d) == m:
		d[d.index(max(d))] = 0
	return max(d)

def amountOfMax(diners):
	cnt = 0
	for i in range(len(diners)):
		if diners[i] == max(diners):
			cnt += 1
	return cnt

def amountOfNum(diners, num):
	cnt = 0
	for i in range(len(diners)):
		if diners[i] == num:
			cnt += 1
	return cnt

def value(num):
	return num // 2 + num % 2


def numGreaterThan(diners, x):
	cnt = 0
	for i in range(len(diners)):
		if diners[i] > x:
			cnt += 1
	return cnt

def count(string):
	tmp = string.split()
	diners = []
	for i in range(len(tmp)):
		diners.append(int(tmp[i]))
	minutes = 0
	m = max(diners)
	# if diners == [5,6,9,6,9,6]:
		# import pdb;pdb.set_trace()
	while max(diners) != 0:
		# if 2 < max(diners) and length(diners) <= max(diners):
		#num of things greater than max//2 < max//2
		if max(diners) == 9 and numGreaterThan(diners, 6) == 1 and secondMax(diners) != 5:
			diners = specialMinutes9(diners)
		elif max(diners) > 2 and numGreaterThan(diners, (max(diners)-max(diners)//2)) < (max(diners)//2):
			minutes += numGreaterThan(diners, (max(diners)-max(diners)//2)) - 1
			# if max(diners) % 2 == 0 and amountOfNum(diners, max(diners)//2+1) != 0:
			# 	minutes -= 1
			upper = (max(diners)-max(diners)//2)
			if max(diners) % 2 == 0 and amountOfMax(diners) == 1 and secondMax(diners) == max(diners) // 2 + 1 and amountOfNum(diners, secondMax(diners)) > 1:
				upper += 1
				minutes -= 2
			for x in range(numGreaterThan(diners, upper)):
				diners = specialMinutes(diners)
		else:
			diners = doNothing(diners)
		minutes += 1
	# if minutes > m:
	# 	return m
	return minutes

def countold(string):
	tmp = string.split()
	diners = []
	for i in range(len(tmp)):
		diners.append(int(tmp[i]))
	minutes = 0
	m = max(diners)
	# if diners == [8,5,5,3]:
	# 	import pdb;pdb.set_trace()
	while max(diners) != 0:
		# if 2 < max(diners) and length(diners) <= max(diners):
		#num of things greater than max//2 < max//2
		if max(diners) == 9 and numGreaterThan(diners, 6) == 1 and secondMax(diners) != 5:
			diners = specialMinutes9(diners)
		elif max(diners) > 2 and numGreaterThan(diners, (max(diners)-max(diners)//2)) < (max(diners)//2):
			minutes += numGreaterThan(diners, (max(diners)-max(diners)//2)) - 1
			for x in range(numGreaterThan(diners, (max(diners)-max(diners)//2))):
				diners = specialMinutes(diners)
		else:
			diners = doNothing(diners)
		minutes += 1
	# if minutes > m:
	# 	return m
	return minutes

def length(diners):
	cnt = 0
	for i in range(len(diners)):
		if diners[i] != 0:
			cnt += 1
	return cnt


def main():
	file1 = open('B-small-attempt8.in','r')
	file2 = open('outfile.txt','w')
	caseNumber = int(file1.readline())
	cases = file1.read().split('\n')
	for x in range(1, caseNumber*2, 2):
		#+ " | " + str(countold(cases[x])) + " | " + cases[x] + 	
		file2.write("Case #" + str((x+1)//2) + ": " + str(count(cases[x])) + "\n")
main()

'''
Case #40: 7 | 8 5 5 3
Case #41: 9 | 9 9 9 9 9 9
Case #42: 5 | 8 4
Case #43: 7 | 8 8 8
Case #44: 5 | 3 5 1 4
Case #45: 8 | 6 6 6 6 9 9
Case #46: 4 | 6
Case #47: 5 | 5 3 4
Case #48: 6 | 6 5 4
Case #49: 6 | 7 7
Case #50: 4 | 5 1 1 3 1
Case #51: 5 | 5 1 2 5 5
Case #52: 6 | 8 3 5
Case #53: 8 | 8 8 8 8 8
Case #54: 8 | 9 4 7 7
Case #55: 5 | 1 1 7
Case #56: 4 | 5
Case #57: 5 | 1 4 6
Case #58: 8 | 5 6 9 6 9 6
Case #59: 5 | 5 5
Case #60: 6 | 3 4 4 9
Case #61: 7 | 3 3 5 5 9 9
Case #62: 8 | 8 9 8 3
Case #63: 5 | 1 5 4 1 3
Case #64: 6 | 8 8 1
Case #65: 6 | 7 3 1 5 1
Case #66: 7 | 7 7 8 3
Case #67: 5 | 1 2 8
Case #68: 4 | 4 3 2 1
Case #69: 5 | 8
Case #70: 5 | 5 2 3 3 5
Case #71: 6 | 9 5 1
Case #72: 6 | 8 8
Case #73: 6 | 9 6
Case #74: 9 | 9 9 9 9
Case #75: 4 | 6 3 2
Case #76: 7 | 9 2 9 5
Case #77: 7 | 9 9
Case #78: 6 | 6 5 4 3 2 1
Case #79: 3 | 4
Case #80: 7 | 1 1 5 5 9 9
Case #81: 6 | 8 1 2 7 1
Case #82: 7 | 1 9 9
Case #83: 7 | 9 7 5
Case #84: 5 | 4 6 2 2
Case #85: 2 | 2 1
Case #86: 3 | 4 1 1
Case #87: 8 | 7 7 7 7 7 9
Case #88: 5 | 5 3 5
Case #89: 7 | 6 8 7 1
Case #90: 5 | 6 6 1
Case #91: 7 | 6 5 1 8
Case #92: 6 | 6 9 1
Case #93: 8 | 8 9 9
Case #94: 7 | 9 8
Case #95: 5 | 4 5 5
Case #96: 3 | 3 1 3
Case #97: 5 | 3 1 5 5 4
Case #98: 5 | 4 8
Case #99: 4 | 2 3 5 2 2
Case #100: 7 | 4 2 9 9

'''
# DeceitfulWar.py
"""
date: 2014-04-12
description: A program solving the 2014 Google Code Jam Problem B.
"""
import string

def readfile(filename):
	fInput = open(filename, 'r')
	lstCases = []

	caseNum = int(fInput.readline())
	for index in range(0, caseNum):
		fInput.readline()
		lstNaomi = string.replace(fInput.readline(), '\n', '').split(' ')
		lstKen = string.replace(fInput.readline(), '\n', '').split(' ')
		lstCases.append([lstNaomi, lstKen])

	return lstCases

def process(lstCases):
	fOutput = open('D-large.out', 'w')
	cnCase = 0

	for case in lstCases:
		cnCase += 1

		n, k = case[0], case[1]
		naomi = [float(x) for x in n]
		ken = [float(x) for x in k]

		fOutput.write('Case #'+str(cnCase)+': ')
		fOutput.write(str(deceitfulwar(naomi[:], ken[:]))+' ')
		fOutput.write(str(war(naomi[:], ken[:]))+'\n')

	fOutput.close()

def war(naomi, ken):
	naomi.sort()
	ken.sort()

	if naomi[0] > ken[-1]:
		return len(naomi)
	elif naomi[-1] < ken[0]:
		return 0

	while len(ken) != 0:
		if naomi[0] > ken[0]:
			ken.remove(ken[0])
		else:
			naomi.remove(naomi[0])
			ken.remove(ken[0])				

	return len(naomi)

def deceitfulwar(naomi, ken):
	naomi.sort()
	ken.sort()

	if naomi[0] > ken[-1]:
		return len(naomi)
	elif naomi[-1] < ken[0]:
		return 0

	naomiWin = 0
	while len(naomi) != 0:
		if naomi[0] < ken[0] or naomi[-1] < ken[-1]: # n is the smallest one of all
			naomi.remove(naomi[0])
			ken.remove(ken[-1])
		else:
			naomi.remove(naomi[0])
			ken.remove(ken[0])
			naomiWin += 1

	return naomiWin
		
def main():
	filename = 'D-large.in'
	process(readfile(filename))

if __name__ == '__main__':
	main()
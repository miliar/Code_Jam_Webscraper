#! c:/Python25/python.exe
# -*- coding: utf-8 -*- 


def hyoka(nAns, tg):
	
		ansText = ""
		if nAns & int('F000', 16) == int('F000', 16):
			ansText = tg + ' won'
		if nAns & int('0F00', 16) == int('0F00', 16):
			ansText = tg + ' won'
		if nAns & int('00F0', 16) == int('00F0', 16):
			ansText = tg + ' won'
		if nAns & int('000F', 16) == int('000F', 16):
			ansText = tg + ' won'
		if nAns & int('8888', 16) == int('8888', 16):
			ansText = tg + ' won'
		if nAns & int('4444', 16) == int('4444', 16):
			ansText = tg + ' won'
		if nAns & int('2222', 16) == int('2222', 16):
			ansText = tg + ' won'
		if nAns & int('1111', 16) == int('1111', 16):
			ansText = tg + ' won'
		if nAns & int('8421', 16) == int('8421', 16):
			ansText = tg + ' won'
		if nAns & int('1248', 16) == int('1248', 16):
			ansText = tg + ' won'

		return ansText


def q1():
	ADD_NUM = [8,4,2,1]


	f = open('data.txt')
	qDat = f.readline()

	maxCnt = int(qDat)

	nCnt = 1
	while qDat:

		#-----------------------------
		
		w = 3
		nAnsX = 0
		nAnsO = 0
		for i in range(0, 4):
			qDat = f.readline()
			
			nX = 0
			nO = 0
			fDraw = 0
			nCharCnt = 0
			for c in qDat:
				if c == 'X':
					nX += ADD_NUM[nCharCnt]
				elif c == 'O':
					nO += ADD_NUM[nCharCnt]
				elif c == 'T':
					nX += ADD_NUM[nCharCnt]
					nO += ADD_NUM[nCharCnt]
				elif c == '.':
					fDraw = 1
				nCharCnt += 1
			
#			print 'X1 = %d : O1 = %d' % (nX, nO)

			nAnsX += nX * pow(16, w)
			nAnsO += nO * pow(16, w)
			w -= 1
			
#			print 'X2 = %d : O2 = %d' % (nAnsX, nAnsO)

		
#		print 'X3 = %s : O3 = %s' % (hex(nAnsX), hex(nAnsO))


		ansText = ""
		ansText = hyoka(nAnsX, 'X')
		if ansText == "":
			ansText = hyoka(nAnsO, 'O')
		if ansText == "" and fDraw == 0:
			ansText = 'Draw'
		if ansText == "":
			ansText = 'Game has not completed'

		print 'Case #%d: %s' % (nCnt, ansText)

		qDat = f.readline()
		nCnt += 1

		if maxCnt < nCnt:
			break

	f.close
	return ""


def main():

#	import time
#	t1 = time.time()

	q1()

#	t2 = time.time()
#	print 'finished'
#	print t2 - t1, 'sec'


if __name__ == "__main__":
	main()

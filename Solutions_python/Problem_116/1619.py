#!/usr/bin/python
import sys



def rows(gato):

	xx=0
	oo=0
	p=0
	for i in range(4):
		for j in range (4):
			if gato[i][j]=='X':
				xx+=1
			elif gato[i][j]=='O':
				oo+=1
			elif gato[i][j]=='T':
				xx+=1
				oo+=1
			elif gato[i][j]=='.':
				p +=1
		if(xx==4):
			return 'X'
		elif (oo == 4):
			return 'O'
		xx=0
		oo=0	

	return p

def cols(gato):
	xx=0
	oo=0
	p=0
	for i in range(4):
		for j in range (4):
			if gato[j][i]=='X':
				xx+=1
			elif gato[j][i]=='O':
				oo+=1
			elif gato[j][i]=='T':
				xx+=1
				oo+=1
			elif gato[i][j]=='.':
				p +=1	
		if(xx==4):
			return 'X'
		elif (oo == 4):
			return 'O'
		xx=0
		oo=0	

	return p

def diagonal1(gato):
	xx=0
	oo=0

	for i in range (4):
		if(gato[i][i]=='X'):
			xx+=1
		elif(gato[i][i]=='O'):
			oo+=1
		elif(gato[i][i]=='T'):
			xx+=1
			oo+=1
	if(xx==4):
		return 'X'
	elif (oo == 4):
		return 'O'


def diagonal2(gato):
	xx=0
	oo=0

	for i in range (4):
		if(gato[i][3-i]=='X'):
			xx+=1
		elif(gato[i][3-i]=='O'):
			oo+=1
		elif(gato[i][3-i]=='T'):
			xx+=1
			oo+=1
	if(xx==4):
		return 'X'
	elif (oo == 4):
		return 'O'
	return False

if __name__ == "__main__":
	
	xx=False
	oo=False
	gato = []
	estado =''
	N = input()
	for test_case in range(N):

		for test in range(4):
			gato.append(raw_input())
		
		colgato = cols(gato)
		rowgato = rows(gato)
		dia1gato = diagonal1(gato)
		dia2gato = diagonal2(gato)
		if colgato =='X':
			xx=True
		if colgato =='O':
			oo=True
		if rowgato =='X':
			xx=True
		if rowgato == 'O':
			oo=True
		if dia1gato == 'X':
			xx=True
		if dia1gato == 'O':
			oo=True
		if dia2gato == 'X':
			xx=True
		if dia2gato == 'O':
			oo=True

		if(xx and oo):
			estado = "Draw"	
		elif(xx==oo):
			if(colgato > 0):
				estado = "Game has not completed"
			else:
				estado = "Draw"
		elif (xx):
			estado = "X won"
		elif (oo):
			estado = "O won"
		print "Case #"+str(test_case+1)+": "+ estado
		
		gato = []
		xx=False
		oo=False
		estado =''
		if test_case < N-1:
			line = raw_input()



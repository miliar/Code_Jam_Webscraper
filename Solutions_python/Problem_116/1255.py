#!/usr/bin/python
import sys

def testonearr(arr):
	if '.' in arr:
		return "."

	if ('X' in arr ) and ('O' in arr ):
		return "Z"

	if 'X' in arr :
		return 'X'
	
	if 'O' in arr:
		return 'O'


def doarr(allin):
	alls = []
	for i in range(0,4):
		alls.append(allin[i][:])
	for i in range(0,4):
		ta = []
		for j in range(0,4):
			ta.append(allin[j][i])
		alls.append(ta)

	arr1 = [allin[3][0],allin[2][1], allin[1][2], allin[0][3]]
	alls.append(arr1)
	arr2 = [allin[0][0],allin[1][1], allin[2][2], allin[3][3]]
	alls.append(arr2)

	res = []
	for line in alls:
		rest = testonearr(line)
		if rest in ['X', 'O'] :
			return rest
		res.append(rest)

	if '.' in res:
		return '.'

	return 'Z'

def treatpart(part, j):
	pres = {"." : "Game has not completed", "X" : "X won", "O" : "O won", "Z" : "Draw"}
	if len(part)!=4:
		return 
	allin = []
	for line in part:
		arr = []
		if len(line) != 4:
			return 
		for i in [0,1,2,3]:
			arr.append(line[i])

		allin.append(arr)
	res = doarr(allin)
	print "Case #%d: %s"%(j, pres[res])

def mainfunc():
	if(len(sys.argv)<2):
		return

	fname = sys.argv[1]
	f = open(fname)
	line=f.readline()
	Ts = int(line.strip())
	
	j=0
	part = []
	while True:
		if(j>Ts):
			return
		line=f.readline()
		if(len(line)<=0):
			break
		
		line = line.strip()
		if(len(line) == 0):
			treatpart(part, j+1)
			part = []
			j+=1
		else:
			part.append(line)
	treatpart(part, j+1)
	
if __name__ == "__main__":
	mainfunc()

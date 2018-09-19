#! /usr/bin/python
import sys

def checkStatus(list1,example,output):
	countX = [0]*10
	countO = [0]*10 
	for i in range(0,4):
		for j in range(0,4):
			if(list1[i][j] in ('X','T') ):
				countX[i] = countX[i]+1
			if(list1[i][j] in ('O','T') ):
				countO[i] = countO[i]+1
	for i in range(0,4):
		for j in range(0,4):
			if(list1[j][i] in ('X','T') ):
				countX[i+4] = countX[i+4]+1
			if(list1[j][i] in ('O','T') ):
				countO[i+4] = countO[i+4]+1
	for i in range(0,4):
		if(list1[i][i] in ('X','T')):
			countX[8] = countX[8]+1
		if(list1[i][i] in ('O','T')):
			countO[8] = countO[8]+1
	for i in range(0,4):
		if(list1[i][3-i] in ('X','T')):
			countX[9] = countX[9]+1
		if(list1[i][3-i] in ('O','T')):
			countO[9] = countO[9]+1
	if ( int(4) in countX ):
		output.write ( 'Case #%d: X won\n'% (example+1))
	elif (int(4) in countO ):
		output.write( 'Case #%d: O won\n'% (example+1))
	else:
		for i in range (0,4):
			if('.' in list1[i]):
				output.write( 'Case #%d: Game has not completed\n'% (example+1))
				return
		output.write('Case #%d: Draw\n'% (example+1))


		

def main():
	sampleList = []
	f = open('A-large.in')
	for i in range(0,1):
		line = f.readline()
		if(i == 0):
			numOfSamples = int(float(line.strip()))
	for j in range(0,numOfSamples):
		list_outer = []
		for i in range(0,4):
			list_inner = []
			line = f.readline()
			line = line.strip()
			for c in line:
				list_inner.append(c.strip())
			list_outer.append(list_inner)
		checkStatus(list_outer,j,sys.stdout)
		line = f.readline()
		
			
			
		
	



if __name__ == '__main__':
  main()
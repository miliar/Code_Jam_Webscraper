import sys
#import math
def ATicTacToeTomek(InputFileName):
	#f=open(InputFileName,"rU")
	lines = open(InputFileName).read().splitlines()
	T=int(lines[0])
	for t in range(1,T+1):
		ListGamePos=[]
		#prepare 4 columns
		for i in range(4):
			ListGamePos.append(list(lines[5*t+i-4]))
			#print ListGamePos[-1]
		#add 4 rows and 2 diagonals
		ListGamePos.extend(zip(*ListGamePos))
		ListGamePos.append([ListGamePos[i][i] for i in range(4)])
		ListGamePos.append([ListGamePos[3-i][i] for i in range(4)])
		# for ListGameLines in ListGamePos:
			# print ''.join(ListGameLines)
		print 'Case #'+str(t)+': ' + StrGameStatus(ListGamePos)
def StrGameStatus(ListGamePosD):
	StrGameStatusF=''
	ListChr=['X', 'O', 'T', '.']
	#check all lines (rows, columns, diagonals):
	for ListLine in ListGamePosD:
		StrLine=''.join(ListLine)
		#check 2 players:
		for Chr in ListChr[:2]:
			#print StrLine, StrLine.replace(Chr,'',3),Chr+ListChr[2], StrLine.replace(Chr,'') in Chr+ListChr[2]
			if StrLine.replace(Chr,'',3) in Chr+ListChr[2]:				
				assert StrGameStatusF=='' or StrGameStatusF==Chr+' won', 'contradiction'
				StrGameStatusF=Chr+' won'
	if StrGameStatusF=='': 
		for ListLine in ListGamePosD:
			if ListChr[3] in StrLine:
				StrGameStatusF='Game has not completed'
		if StrGameStatusF=='':
			StrGameStatusF='Draw'
	return StrGameStatusF
def main():
	if len(sys.argv)==2: ATicTacToeTomek(sys.argv[1])
	else: ATicTacToeTomek('A-example.in')
if __name__ == '__main__':
	main()
	

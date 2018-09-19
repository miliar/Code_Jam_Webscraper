import sys

file = open('input.txt', 'r')
testcase=int(file.readline())
#print testcase
case=1
while case <=testcase:
	line=file.readline()
	line=line.strip()
	C,F,X=map(float,line.split())
	
	#print C , F ,X
	initialf=F
	F=2
	time=0
	while (X/F) > ((C/F)+(X/(F+initialf))):
		time=time+(C/F)
		F=F+initialf
	time=time+(X/F)
	resultstr="Case #"+str(case)+": "
	print resultstr+ "%0.7f" % time
	case=case+1

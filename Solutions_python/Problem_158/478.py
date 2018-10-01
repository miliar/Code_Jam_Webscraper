# Windows 8.1 python 2.7.9

#inFile = "pDs.in"
#inFile  = "D-small-attempt1.in"
inFile  = "D-large.in"

with open(inFile) as inF:
    contents = inF.readlines()

numCases = int(contents[0])
for case in range(1,numCases+1):
    thisCase = contents[case].split()
    X = int(thisCase[0])
    R = int(thisCase[1])
    C = int(thisCase[2])
    if X == 1:
	winner = 'GABRIEL'
    elif ( (X>R and X>C) or (X%2==0 and (R*C)%2!=0) or (X%2!=0 and (R*C)%X!=0) or (X>2 and (R==1 or C==1)) or (X==4 and (R*C)==8) ):
	winner = 'RICHARD'
    elif ( (X>6) or (X==5 and (R*C)==15) or ((R*C)%X!=0) or ((X+1)/2>min(R,C)) or (X==6 and 3 >= min(R,C)) ):
	winner = 'RICHARD'
    else:
	winner = 'GABRIEL'

    print 'Case #{0:d}: {1:s}'.format(case,winner)


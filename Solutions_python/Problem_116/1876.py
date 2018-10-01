def ch(ar):
	#hor
	for i in range(0,4):
		xc=0;oc=0;tc=0;
		for j in range(0,4):
			if ar[i][j]=="X":xc+=1
			if ar[i][j]=="T":tc+=1
			if ar[i][j]=="O":oc+=1
		if xc+tc==4:
			return "X won"
		if oc+tc==4:
			return "O won"
	#ver
	for i in range(0,4):
		xc=0;oc=0;tc=0;
		for j in range(0,4):
			if ar[j][i]=="X":xc+=1
			if ar[j][i]=="T":tc+=1
			if ar[j][i]=="O":oc+=1
		if xc+tc==4:
			return "X won"
		if oc+tc==4:
			return "O won"
	#diagdown
	y=0
	xc=0;oc=0;tc=0;
	for x in range(4):
		if ar[y+x][x]=="X":xc+=1
		if ar[y+x][x]=="T":tc+=1
		if ar[y+x][x]=="O":oc+=1
	if xc+tc==4:
		return "X won"
	if oc+tc==4:
		return "O won"
	#diagup
	y=3
	xc=0;oc=0;tc=0;
	for x in range(4):
		if ar[y-x][x]=="X":xc+=1
		if ar[y-x][x]=="T":tc+=1
		if ar[y-x][x]=="O":oc+=1
	if xc+tc==4:
		return "X won"
	if oc+tc==4:
		return "O won"

	for x in ar:
		if "." in x:
			return "Game has not completed"
	return "Draw"

c=int(input())
for i in range(c):
	ar=["."]*4
	for j in range(4):
		l=input().split()
		for x in range(len(l)):
			ar[j]=l[x]
	print ("Case #"+str(i+1)+": "+ch(ar))
	if i!=c-1: input()








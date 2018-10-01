import sys
sys.stdin = open("in.txt","r")
sys.stdout = open("out.txt","w")
for t in range(int(input())) :
	n,r,o,y,g,b,v = map(int,input().split())
	ls = [[r,'R'],[y,'Y'],[b,'B']]
	ls = sorted(ls)[::-1]
	if ls[0][0] > ls[1][0] + ls[2][0] :
		s = 'IMPOSSIBLE'
	elif ls[0][0] == ls[1][0] + ls[2][0] : 
		s = (ls[0][1]+ls[1][1])*(ls[1][0]) + (ls[0][1]+ls[2][1])*(ls[2][0])
	else : 
		s = (ls[2][0] - ls[0][0] + ls[1][0])*(ls[0][1]+ls[1][1]+ls[2][1])
		s += (ls[0][0] - ls[2][0])*(ls[0][1]+ls[1][1])
		s += (ls[0][0] - ls[1][0])*(ls[0][1]+ls[2][1])
	print('Case #',t+1,': ' ,s,sep = '')	
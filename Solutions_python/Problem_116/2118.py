# Coded by @alexdev_

def judge(str):
	# Horizontal Test
	for x in range(0,4):
		rank=0
		for y in range(0,4):			
			if str[x][y]=="T" or str[x][y]=="O":
				rank+=1
		if rank==4: return "O won"

		rank=0
		for y in range(0,4):			
			if str[x][y]=="T" or str[x][y]=="X":
				rank+=1
		if rank==4: return "X won"
	# Vertical Test
	for y in range(0,4):
		rank=0
		for x in range(0,4):
			if str[x][y]=="T" or str[x][y]=="O":
				rank+=1
		if rank==4: return "O won"

		rank=0
		for x in range(0,4):			
			if str[x][y]=="T" or str[x][y]=="X":
				rank+=1
		if rank==4: return "X won"

	# cross1
	rankx=0
	ranko=0
	for x in range(0,4):
		if str[x][x]=="T" or str[x][x]=="O":
			ranko+=1
		if str[x][x]=="T" or str[x][x]=="X":
			rankx+=1
	# print rank
	if ranko==4: return "O won"
	if rankx==4: return "X won"
	# cross2
	rankx=0
	ranko=0
	for x in range(0,4):
		# print str[x][3-x]
		if str[x][3-x]=="T" or str[x][3-x]=="X":
			rankx+=1
		if str[x][3-x]=="T" or str[x][3-x]=="O":
			ranko+=1
	if rankx==4: return "X won"	
	if ranko==4: return "O won"
# else
	complete=True
	for x in range(0,4):
		for y in range(0,4):
			if str[x][y]=='.':
				complete=False
	if complete==True:
		return "Draw"
	else:
		return "Game has not completed"

def main():
	input=open("A-large.in",'r')
	output=open("1.out","w")

	total=int(input.readline())
	str=[1,1,1,1,1]
	for i in range(1,total+1):
		for x in range(0,5):
			str[x]=input.readline()
			# print str[x],
		result=judge(str)
		print "Case #%d: %s" %(i, result)
		output.write("Case #%d: %s\n" %(i, result))
main()

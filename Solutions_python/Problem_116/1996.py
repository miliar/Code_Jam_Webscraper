loop = input()
num = 1
while loop>0:
	count = 1
	inpo = ""
	while count<=4:
		inp = raw_input()
		inp = inpo+inp
		inpo = inp
		count = count+1
	inp2 = inp
	gameset = "Game has not completed"
	
	inp = inp.replace("T", "X")
	if inp[0] == inp[1] == inp[2] == inp[3] and inp[0]+inp[1]+inp[2]+inp[3] != "....":
		gameset = inp[0]+" won"
	if inp[4] == inp[5] == inp[6] == inp[7] and inp[4]+inp[5]+inp[6]+inp[7] != "....":
		gameset = inp[4]+" won"
	if inp[8] == inp[9] == inp[10] == inp[11] and inp[8]+inp[9]+inp[10]+inp[11] != "....":
		gameset = inp[8]+" won"
	if inp[12] == inp[13] == inp[14] == inp[15] and inp[12]+inp[13]+inp[14]+inp[15] != "....":
		gameset = inp[12]+" won"

	if inp[0] == inp[4] == inp[8] == inp[12] and inp[0]+inp[4]+inp[8]+inp[12] != "....":
		gameset = inp[0]+" won"
	if inp[1] == inp[5] == inp[9] == inp[13] and inp[1]+inp[5]+inp[9]+inp[13] != "....":
		gameset = inp[1]+" won"
	if inp[2] == inp[6] == inp[10] == inp[14] and inp[2]+inp[6]+inp[10]+inp[14] != "....":
		gameset = inp[2]+" won"
	if inp[3] == inp[7] == inp[11] == inp[15] and inp[3]+inp[7]+inp[11]+inp[15] != "....":
		gameset = inp[3]+" won"

	if inp[0] == inp[5] == inp[10] == inp[15] and inp[0]+inp[5]+inp[10]+inp[15] != "....":
		gameset = inp[0]+" won"
	if inp[3] == inp[6] == inp[9] == inp[12] and inp[3]+inp[6]+inp[9]+inp[12] != "....":
		gameset = inp[3]+" won"
	
	inp = inp2.replace("T", "O")
	if inp[0] == inp[1] == inp[2] == inp[3] and inp[0]+inp[1]+inp[2]+inp[3] != "....":
		gameset = inp[0]+" won"
	if inp[4] == inp[5] == inp[6] == inp[7] and inp[4]+inp[5]+inp[6]+inp[7] != "....":
		gameset = inp[4]+" won"
	if inp[8] == inp[9] == inp[10] == inp[11] and inp[8]+inp[9]+inp[10]+inp[11] != "....":
		gameset = inp[8]+" won"
	if inp[12] == inp[13] == inp[14] == inp[15] and inp[12]+inp[13]+inp[14]+inp[15] != "....":
		gameset = inp[12]+" won"

	if inp[0] == inp[4] == inp[8] == inp[12] and inp[0]+inp[4]+inp[8]+inp[12] != "....":
		gameset = inp[0]+" won"
	if inp[1] == inp[5] == inp[9] == inp[13] and inp[1]+inp[5]+inp[9]+inp[13] != "....":
		gameset = inp[1]+" won"
	if inp[2] == inp[6] == inp[10] == inp[14] and inp[2]+inp[6]+inp[10]+inp[14] != "....":
		gameset = inp[2]+" won"
	if inp[3] == inp[7] == inp[11] == inp[15] and inp[3]+inp[7]+inp[11]+inp[15] != "....":
		gameset = inp[3]+" won"

	if inp[0] == inp[5] == inp[10] == inp[15] and inp[0]+inp[5]+inp[10]+inp[15] != "....":
		gameset = inp[0]+" won"
	if inp[3] == inp[6] == inp[9] == inp[12] and inp[3]+inp[6]+inp[9]+inp[12] != "....":
		gameset = inp[3]+" won"
	
	if gameset == "Game has not completed":
		inp = inp.replace("O", "T")
		inp = inp.replace("X", "T")
		if inp[0] == inp[1] == inp[2] == inp[3] == inp[4] == inp[5] == inp[6] == inp[7] == inp[8] == inp[9] == inp[10] == inp[11] == inp[12] == inp[13] == inp[14] == inp[15]:
			gameset = "Draw"
		if "." in str(inp):
			gameset = "Game has not completed"
		

	
	nums = str(num)
	gameset = str(gameset)
	print "Case #"+nums+": "+gameset
	raw_input()
	num = num+1
	loop = loop-1
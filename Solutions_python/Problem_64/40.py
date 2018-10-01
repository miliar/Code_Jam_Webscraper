T = int(raw_input())
fileobj = open("3op.txt","w")
for t in range(1,T+1):

	inp = raw_input().split(' ')
	M = int(inp[0])
	N = int(inp[1])
	res={}
	total=0
	board=[]
	occupied= []
	for i in range(M):
		temp = int("0x"+raw_input(),16)
		temp_bin = bin(temp)
		temp_bin = temp_bin[2:len(temp_bin)]
		if len(temp_bin) != N:
			d= N-len(temp_bin)
			temp_bin= '0'*d+temp_bin
		board.append( temp_bin )
		occ=[]
		for j in range(N):
			occ.append(0)
		occupied.append(occ)

	for i in range(min(M-1,N-1),-1,-1):
		curr_board=[]
		curr_board_size=i+1
		no_of_possible_squares_x= M-i
		no_of_possible_squares_y= N-i
		#print curr_board_size ,no_of_possible_squares_x,no_of_possible_squares_y
		for each_start_x in range(0,no_of_possible_squares_x):
			for each_start_y in range(0,no_of_possible_squares_y):
				flag=0
				prev = ''
				for each_y_cell in range(each_start_y,each_start_y+curr_board_size):
					for each_x_cell in range(each_start_x,each_start_x+curr_board_size):

						if each_y_cell != each_start_y:
							prev=  board[each_x_cell][each_y_cell-1]
						curr_pos = board[each_x_cell][each_y_cell]
						#if prev !='':
						if (curr_pos == prev) or (occupied[each_x_cell][each_y_cell] == 1):
							flag=1
							break
						prev = curr_pos
					if flag==1:
						break
				if flag == 0:
					if curr_board_size not in res.keys():
						res[curr_board_size] = 1
					else:
						res[curr_board_size] = res[curr_board_size] +1
					total=total+1
					for each_y_cell in range(each_start_y,each_start_y+curr_board_size):
						for each_x_cell in range(each_start_x,each_start_x+curr_board_size):
							occupied[each_x_cell][each_y_cell] = 1


	fileobj.write( "Case #"+str(t)+": "+str(len(res.keys()))+"\n")
	for x in sorted(res.keys(),reverse=True):
		fileobj.write(str(x)+" "+str(res[x])+"\n")
		
	#fileobj.write( "Case #"+str(t)+": "+str(total))
fileobj.close()
	

if __name__ == "__main__":
	with open("A-small-attempt1.in", 'r') as inputf:
		outputf=open("A_out.out",'w')
		line=inputf.readline()
		line=line.rstrip('\n')
		test_num=int(line)
		
		for test in range(test_num):
			line = inputf.readline()
			line = line.rstrip('\n')
			n = int(line)
			analysis = [[[[]]],[[[]]]]
			j = [0, 0]

			for i in range(n):
				line = inputf.readline()
				line = line.rstrip('\n')
				temp = line[0]
				analysis[i][0][0]=temp
				count = 0
				char_c = len(line)
				for char in line:
					if char == temp:
						count = count + 1
					else:
						analysis[i][j[i]].append(count)
						temp = char
						j[i] = j[i]+1
						count = 1
						analysis[i].append([temp])
					char_c = char_c-1
					if char_c == 0:
						analysis[i][j[i]].append(count)

			change = 0
			pos = True
			if j[0]!=j[1]:
				result = "Case #%d: Fegla Won"%(test+1)
				outputf.write(result)
				pos = False
			else:
				for k in range(j[0]+1):
					if analysis[0][k][0] != analysis[1][k][0]:
						result = "Case #%d: Fegla Won"%(test+1)
						outputf.write(result)
						pos = False
						break
					else:
						if analysis[0][k][1] > analysis[1][k][1]:
							change = change + analysis[0][k][1] - analysis[1][k][1]
						else:
							change = change - analysis[0][k][1] + analysis[1][k][1]

			if pos == True:
				result = "Case #%d: %d" %(test+1, change)
				outputf.write(result)

			if test != test_num - 1:
				outputf.write('\n')








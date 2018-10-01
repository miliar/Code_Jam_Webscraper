#!/usr/bin/python
import string

def process_lines(lines, cs):
	print lines
	return check_row(lines, cs)
	
def check_row(lines, cs):
	x_r_counter = [0,0,0,0]
	y_r_counter = [0,0,0,0]
	x_c_counter = [0,0,0,0]
	y_c_counter = [0,0,0,0]
	x_d_r_counter = 0
	y_d_r_counter = 0
	x_d_l_counter = 0
	y_d_l_counter = 0
	l_diagonal  = 0  
	r_diagonal  = 0  
	row         = 0
	for i in range(16):
		#check row
		if i % 4 == 0:
			r_diagonal  = r_diagonal + 3
			if i != 0:
				row = row + 1 
				l_diagonal = l_diagonal + 5

		if lines[i] == 'X' or lines[i] == 'T':
			x_r_counter[row] = x_r_counter[row] + 1 
		if lines[i] == 'O' or lines[i] == 'T':
			y_r_counter[row] = y_r_counter[row] + 1 
		if x_r_counter[row] == 4:
			return 'Case #%d: X won\r\n'%cs
		if y_r_counter[row] == 4:
			return 'Case #%d: O won\r\n'%cs
		
		#check column
		j = i % 4
		if lines[i] == 'X' or lines[i] == 'T':
			x_c_counter[j] = x_c_counter[j] + 1 
		if lines[i] == 'O' or lines[i] == 'T':
			y_c_counter[j] = y_c_counter[j] + 1 
		if 4 in x_c_counter:
			return 'Case #%d: X won\r\n'%cs
		if 4 in y_c_counter:
			return 'Case #%d: O won\r\n'%cs
			
		#check diagonal
		if i == l_diagonal:
			if lines[i] == 'X' or lines[i] == 'T':
				x_d_l_counter = x_d_l_counter + 1
			if lines[i] == 'O' or lines[i] == 'T':
				y_d_l_counter = y_d_l_counter + 1
				
		if i == r_diagonal:
			if lines[i] == 'X' or lines[i] == 'T':
				x_d_r_counter = x_d_r_counter + 1
			if lines[i] == 'O' or lines[i] == 'T':
				y_d_r_counter = y_d_r_counter + 1
		
		if x_d_l_counter == 4:
			return 'Case #%d: X won\r\n'%cs
		if y_d_l_counter == 4:
			return 'Case #%d: O won\r\n'%cs
		if x_d_r_counter == 4:
			return 'Case #%d: X won\r\n'%cs
		if y_d_r_counter == 4:
			return 'Case #%d: O won\r\n'%cs
	if '.' in lines:
		return 'Case #%d: Game has not completed\r\n'%cs
	else:
		return 'Case #%d: Draw\r\n'%cs
	return ''
	
def main():
	i_file = open('google_q1.txt', 'r')
	o_file = open('google_q1_out.txt', 'w')
	T = int(i_file.readline().split()[0])
	for i in range(T):
		lines = [] 
		for j in range(4):
			line = i_file.readline().split()
			line = string.join(line, '')
			line = list(line)
			for l in line:
				lines.append(l)
		# read blank line	
		i_file.readline()
		s = process_lines(lines, i+1)
		o_file.write(s)
		
	i_file.close()
	o_file.close()
	print 'End'

if __name__ == "__main__":
    main()

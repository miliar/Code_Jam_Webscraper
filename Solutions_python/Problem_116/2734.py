def check_horizontal(rows):
	out_check = None
	for i in range(0,16,4):
		j = 0
		check = None
		while j < 4:
			k = i+j
			if rows[k] == '.':
				check = "Dot"
				break
			else:
				if check == None:
					check = rows[k]
				elif check == rows[k] or rows[k] == 'T' or check == 'T':
					if rows[k] == 'X' or rows[k] == 'O':
						check = rows[k]
				else:
					check = None
					break

			j += 1

		if check == 'X' or check == 'O':
			return check

	for i in rows:
		if i == '.':
			out_check = "Dot"		

	return out_check

def check_vertical(rows):
	out_check = None
	for i in range(0,4):
		check = None
		for j in range(i,16,4):
			if rows[j] == '.':
				check = "Dot"
				break
			else:
				if check == None:
					check = rows[j]
				elif check == rows[j] or rows[j] == 'T' or check == 'T':
					if rows[j] == 'X' or rows[j] == 'O':
						check = rows[j]
				else:
					check = None
					break

		if check == 'X' or check == 'O':
			return check

	for i in rows:
		if i == '.':
			out_check = "Dot"

	return out_check


def check_diagonal(rows):
	out_check = None
	check = None
	for j in range(0,16,5):
		if rows[j] == '.':
			check = "Dot"
			break
		else:
			if check == None:
				check = rows[j]
			elif check == rows[j] or rows[j] == 'T' or check == 'T':
				if rows[j] == 'X' or rows[j] == 'O':
					check = rows[j]
			else:
				check = None
				break

	if check == 'X' or check == 'O':
		return check


	check = None
	count = 0
	for j in range(3,16,3):
		count += 1
		if count == 4:
			break
		if rows[j] == '.':
			check = "Dot"
			break
		else:
			if check == None:
				check = rows[j]
			elif check == rows[j] or rows[j] == 'T' or check == 'T':
				if rows[j] == 'X' or rows[j] == 'O':
					check = rows[j]
			else:
				check = None
				break

	if check == 'X' or check == 'O':
		return check

	for i in rows:
		if i == '.':
			out_check = "Dot"

	return out_check


if __name__ == "__main__":
	t = input()
	for i in range(0,t):
		check_hor = None
		check_ver = None
		check_dia = None
		rows = []
		for j in range(0,4):
			temp = raw_input()
			for k in temp:
				rows.append(k)

		if i < t-1:
			temp = raw_input()

		check_hor =  check_horizontal(rows)
		if check_hor == 'X' or check_hor == 'O':
			out = "Case #" + str(i+1) + ": " + str(check_hor) + " won"
			print out
		else:
			check_ver = check_vertical(rows)
			if check_ver == 'X' or check_ver == 'O':
				out = "Case #" + str(i+1) + ": " + str(check_ver) + " won"
				print out
			else:
				check_dia = check_diagonal(rows)
				if check_dia == 'X' or check_dia == 'O':
					out = "Case #" + str(i+1) + ": " + str(check_dia) + " won"
					print out
				else:
					if check_hor == None:
						out = "Case #" + str(i+1) + ": Draw" 
						print out	
					elif check_hor == "Dot":
						out = "Case #" + str(i+1) + ": Game has not completed" 
						print out	



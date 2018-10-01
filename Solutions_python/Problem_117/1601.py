#! /usr/bin/python3
# VIC Nicolas - Qualification Round: Problem A for the Google CodeJam 2013

counter = 1
def print_case(string):
	global counter
	print("Case #{}: {}".format(counter, string))
	counter = counter + 1

def build_lawn():
	size = [input().split(), []]
	for height in range(int(size[0][0])):
		size[1].append(input().split())

	return size

def eval_lawn(lawn):
	lawn_height = lawn[1]

	#prealoc array of validity
	validity = []
	for i in range(int(lawn[0][0])):
		array = []
		for j in range(int(lawn[0][1])):
			array.insert(j, 'N')
		validity.append(array)

#pour chaque case
#cherche si tout les elements de la ligne/column sont <= , alors la case est VRAI
#si il reste une case a FAUX, le tableau est FAUX
	for line in range(int(lawn[0][0])):
		for column in range(int(lawn[0][1])):
			if eval_line(line, column, lawn) == 1 \
			or eval_column(line, column, lawn) == 1:
				validity[line][column] = 'Y'


	for line in range(int(lawn[0][0])):
		for column in range(int(lawn[0][1])):
			if validity[line][column] == 'N':
				print_case("NO")
				return
			
	print_case("YES")
	return
	
	

def eval_line(line, column, lawn):
	for column_i in range(int(lawn[0][1])):
		if lawn[1][line][column] < lawn[1][line][column_i]:
			return 0
	return 1

def eval_column(line, column, lawn):
	for line_i in range(int(lawn[0][0])):
		if lawn[1][line][column] < lawn[1][line_i][column]:
			return 0
	return 1

total_problems = int(input())

for i in range(total_problems):
	lawn = build_lawn()
	eval_lawn(lawn)


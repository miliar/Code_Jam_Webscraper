#input_lines = open("tmp.in").read().splitlines()
#input_lines = open("A-small-attempt0.in").read().splitlines()
#input_lines = open("A-large-attempt0.in").read().splitlines()
#input_lines = open("B-small-attempt0.in").read().splitlines()
#input_lines = open("B-large-attempt0.in").read().splitlines()
#input_lines = open("C-small-attempt0.in").read().splitlines()
#input_lines = open("C-large-attempt0.in").read().splitlines()
input_lines = open("D-small-attempt3.in").read().splitlines()
#input_lines = open("D-large-attempt0.in").read().splitlines()

test_num = int(input_lines[0])
winner=""
for i in range(test_num):
	x,r,c = map(int, input_lines[i+1].split())
	if x == 1:
		winner = "GABRIEL"
	elif x == 2:
		if r*c % 2 != 0:
			winner = "RICHARD"
		else:
			winner = "GABRIEL"
	elif x == 3:
		if r*c % 3 != 0 or r*c < 6:
			winner = "RICHARD"
		else:
			winner = "GABRIEL"

	else:
		if r*c % 4 !=0  or r*c < 12:
			winner = "RICHARD"
		else:
			winner = "GABRIEL"
		

	print "Case #" + str(i+1) + ": " + winner

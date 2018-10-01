f = open('D-small-attempt1.in', 'r');
o = open('output', 'w');

def omino(sentence, count):
	sentence = sentence.replace('\n', '').split(" ");
	print sentence;
	line = [int(numeric_string) for numeric_string in sentence];
	x = line[0];
	r = line[1];
	c = line[2];
	dim = [r, c];
	winner = "GABRIEL";
	if x > r*c or (r*c) % x != 0:
		winner = "RICHARD";
	elif x == 3:
		if dim == [1,3] or dim == [3,1]:
			winner = "RICHARD";

	elif x ==4:
		if dim == [2,2] or dim == [2,4] or dim == [4,2] or dim == [1,4] or dim == [4,1]:
			winner = "RICHARD";

	o.write('Case #' + str(count) + ': ' + winner + '\n');

case_number = 1
for x in f.readlines()[1:]:
  omino(x, case_number);
  case_number += 1;
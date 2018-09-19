def convert_alphabet(char):
	if 'a' == char:
		return 'y'
	elif 'b' == char:
		return 'h'
	elif 'c' == char:
		return 'e'
	elif 'd' == char:
		return 's'
	elif 'e' == char:
		return 'o'
	elif 'f' == char:
		return 'c'
	elif 'g' == char:
		return 'v'
	elif 'h' == char:
		return 'x'
	elif 'i' == char:
		return 'd'
	elif 'j' == char:
		return 'u'
	elif 'k' == char:
		return 'i'
	elif 'l' == char:
		return 'g'
	elif 'm' == char:
		return 'l'
	elif 'n' == char:
		return 'b'
	elif 'o' == char:
		return 'k'	
	elif 'p' == char:
		return 'r'
	elif 'q' == char:
		return 'z'
	elif 'r' == char:
		return 't'
	elif 's' == char:
		return 'n'
	elif 't' == char:
		return 'w'
	elif 'u' == char:
		return 'j'
	elif 'v' == char:
		return 'p'
	elif 'w' == char:
		return 'f'
	elif 'x' == char:
		return 'm'
	elif 'y' == char:
		return 'a'
	elif 'z' == char:
		return 'q'

def translate_word(sentence):
	new_sentence = ''
	for char in sentence:
		if char == '\n':
			return new_sentence
		if char != ' ':
			nchar =convert_alphabet(char)
			print 'nuevo ', nchar
			new_sentence = new_sentence + nchar
		else:
			print 'paso'
			new_sentence = new_sentence + ' '
	return new_sentence

file = open("A-small-attempt0.in", "r+")
ofile = open("output.txt","w+")
number = 0 # number of test
count= 0
for line in file:
	if count == 0:
		number = int(line)
		count +=1
	else:
		sentence = translate_word(line)
		ofile.write("Case #"+str(count)+": " + sentence +'\n')
		count +=1
file.close()
ofile.close()
	
	

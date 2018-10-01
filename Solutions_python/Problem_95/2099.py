f = open('A-small-attempt0.in','r')

numinputs = int(f.readline())

def translatetoenglish(line):
	completeline = ""
	for letter in line:
		if letter == '\n':
			break	
		elif letter == ' ':
			completeline += ' '
		elif letter == 'a':
			completeline += 'y'
		elif letter == 'b':
			completeline += 'h'
		elif letter == 'c':
			completeline += 'e'
		elif letter == 'd':
			completeline += 's'
		elif letter == 'e':
			completeline += 'o'
		elif letter == 'f':
			completeline += 'c'
		elif letter == 'g':
			completeline += 'v'
		elif letter == 'h':
			completeline += 'x'
		elif letter == 'i':
			completeline += 'd'
		elif letter == 'j':
			completeline += 'u'
		elif letter == 'k':
			completeline += 'i'
		elif letter == 'l':
			completeline += 'g'			
		elif letter == 'm':
			completeline += 'l'			
		elif letter == 'n':
			completeline += 'b'
		elif letter == 'o':
			completeline += 'k'
		elif letter == 'p':
			completeline += 'r'
		elif letter == 'q':
			completeline += 'z'
		elif letter == 'r':
			completeline += 't'
		elif letter == 's':
			completeline += 'n'
		elif letter == 't':
			completeline += 'w'
		elif letter == 'u':
			completeline += 'j'
		elif letter == 'v':
			completeline += 'p'
		elif letter == 'w':
			completeline += 'f'
		elif letter == 'x':
			completeline += 'm'
		elif letter == 'y':
			completeline += 'a'
		elif letter == 'z':
			completeline += 'q'
	return completeline
			
for x in range(0,numinputs):
	line = f.readline()
	print "Case #" + str(x+1) + ": " + translatetoenglish(line)

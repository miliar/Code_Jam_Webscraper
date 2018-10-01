
def ungooglerese(c):
	options = {
		'a' : 'y',
		'b' : 'h',
		'c' : 'e',
		'd' : 's',
		'e' : 'o',
		'f' : 'c',
		'g' : 'v',
		'h' : 'x',
		'i' : 'd',
		'j' : 'u',
		'k' : 'i',
		'l' : 'g',
		'm' : 'l',
		'n' : 'b',
		'o' : 'k',
		'p' : 'r',
		'q' : 'z',
		'r' : 't',
		's' : 'n',
		't' : 'w',
		'u' : 'j',
		'v' : 'p',
		'w' : 'f',
		'x' : 'm',
		'y' : 'a',
		'z' : 'q',
		' ' : ' '
	}
	return options[c]
	
def main():
	finput = open("A-small-attempt0.in", 'r')
	foutput = open("output.txt", 'w')
	
	T = int(finput.readline())
	for case in range(T):
		if case == 31:
			break
		G = finput.readline().rstrip('\n')
		S = map(ungooglerese, G) 
		foutput.write('Case #' + str(case+1) + ': ' + ''.join(S) + '\n')
	
	foutput.close()
	finput.close()		
			


if '__main__' == __name__ :
	main()

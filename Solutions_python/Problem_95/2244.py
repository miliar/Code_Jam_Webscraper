# Ben Shippee 
# FirewallXIII

# GCJ 12 A
global fixed 
fixed = []
def decode(strings):
	for string in strings:
		s = []
		i = 0
		while i< len(string):
			if(string[i] == 'y'):
				s.append('a')
			elif (string[i] == 'n'):
				s.append('b')
			elif (string[i] == 'f'):
				s.append('c')
			elif (string[i] == 'i'):
				s.append('d')
			elif (string[i] == 'c'):
				s.append('e')
			elif (string[i] == 'w'):
				s.append('f')
			elif (string[i] == 'l'):
				s.append('g')
			elif (string[i] == 'b'):
				s.append('h')
			elif (string[i] == 'k'):
				s.append('i')
			elif (string[i] == 'u'):
				s.append('j')
			elif (string[i] == 'o'):
				s.append('k')
			elif (string[i] == 'm'):
				s.append('l')
			elif (string[i] == 'x'):
				s.append('m')
			elif (string[i] == 's'):
				s.append('n')
			elif (string[i] == 'e'):
				s.append('o')
			elif (string[i] == 'v'):
				s.append('p')
			elif (string[i] == 'z'):
				s.append('q')
			elif (string[i] == 'p'):
				s.append('r')
			elif (string[i] == 'd'):
				s.append('s')
			elif (string[i] == 'r'):
				s.append('t')
			elif (string[i] == 'j'):
				s.append('u')
			elif (string[i] == 'g'):
				s.append('v')
			elif (string[i] == 't'):
				s.append('w')
			elif (string[i] == 'h'):
				s.append('x')
			elif (string[i] == 'a'):
				s.append('y')
			elif (string[i] == 'q'):
				s.append('z')
			elif(string[i] == ' '):
				s.append(' ')
			i+=1
		fixed.append("".join(s))

strings = []
n = int(raw_input())
i = 0
while i < n:
    new_string = raw_input()
    if new_string not in strings:
        strings.append(new_string)
    i+= 1
decode(strings)
i = 0
while i < n:
	print  "Case #"+str(i+1)+": "+fixed[i]
	i += 1
	
mapper = {'q': 'z', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}
 
translated = ''
case = input('')
for j in range(case):
	translated = ''
	googleres = raw_input('')
	for i in range(len(googleres)):
		if googleres[i] == ' ':
			translated += ' '
		else:
			translated += mapper[googleres[i]]
	print "Case #" + str(j+1) + ": " + translated
	
	
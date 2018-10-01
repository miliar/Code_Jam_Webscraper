def ggltranslate(sentence):
	gglrese = {
		'a' : 'y', 'b' : 'h', 
		'c' : 'e', 'd' : 's',
		'e' : 'o', 'f' : 'c', 
		'g' : 'v', 'h' : 'x',
		'i' : 'd', 'j' : 'u', 
		'k' : 'i', 'l' : 'g',
		'm' : 'l', 'n' : 'b', 
		'o' : 'k', 'p' : 'r',
		'q' : 'z', 'r' : 't', 
		's' : 'n', 't' : 'w',
		'u' : 'j', 'v' : 'p', 
		'w' : 'f', 'x' : 'm', 
		'y' : 'a', 'z' : 'q', 
		' ' : ' ', ',' : ',', 
		'\n' : ''
	}
	x = ''
	for let in sentence:
		x+=(gglrese[let])
	return x

lines = open("asmall12012.input").readlines()
for case in range(1, 31):
	line = lines[case-1]
	print "Case #%d: %s" % (case, ggltranslate(line))

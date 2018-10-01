import sys
dictGtoEng = {'a':'y',
		'b':'h',
		'c':'e',
		'd':'s',
		'e':'o',
		'f':'c',
		'g':'v',
		'h':'x',
		'i':'d',
		'j':'u',
		'k':'i',
		'l':'g',
		'm':'l',
		'n':'b',
		'o':'k',
		'p':'r',
		'q':'z',
		'r':'t',
		's':'n',
		't':'w',
		'u':'j',
		'v':'p',
		'w':'f',
		'x':'m',
		'y':'a',
		'z':'q'}
		
if len(sys.argv) > 1:
	filename = sys.argv[1]
	f = open(filename,'r')
	count = 0
	
	outF = open('greeseout.txt','w+')
	
	for line in f.readlines():
		if count != 0:
			out = "Case #%d: " % count 
		 	for char in line:
		 		if dictGtoEng.has_key(char):
			 		out = out + dictGtoEng[char]
			 	else:
			 		out = out + char
		 	out = out 
		 	print out
		 	outF.write(out)
		 	outF.flush()
		 	count = count + 1
		else:
		 	count = count + 1
		 	
		
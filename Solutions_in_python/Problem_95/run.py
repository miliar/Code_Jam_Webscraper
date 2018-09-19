#by sample
dictionary = {
	"y":"a",
	"n":"b",
	"f":"c",
	"i":"d",
	"c":"e",
	"w":"f",
	"l":"g",
	"b":"h",
	"k":"i",
	"u":"j",
	"o":"k",
	"m":"l",
	"x":"m",
	"s":"n",			
	"e":"o",
	"v":"p",
	"q":"z",#
	"p":"r",
	"d":"s",
	"r":"t",
	"j":"u",
	"g":"v",
	"t":"w",
	"h":"x",
	"a":"y",
	"z":"q"#
}

def translate(w):
	res = ""
	for k in w:
		res = res+dictionary[k]
	return res

T = input()

for i in xrange(0, T):
	inp = raw_input()
	words = inp.split(" ")	
	out = ""
	for word in words:
		out = out+translate(word)+" "
	out = out[:-1]

	print 'Case #%(iteration)i: %(result)s'%{'iteration':i+1, 'result':out}
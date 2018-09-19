
import sys


def runme():
	alphadict = {
		"a": "y",
		"b": "h", 
		"c": "e",
		"d": "s",
		"e": "o",
		"f": "c",
		"g": "v",
		"h": "x",
		"i": "d",
		"j": "u",
		"k": "i",
		"l": "g",
		"m": "l",
		"n": "b", 
		"o": "k", 
		"p": "r", 
		"q": "z",
		"r": "t",
		"s": "n",
		"t": "w",
		"u": "j",
		"v": "p", 
		"w": "f",
		"x": "m",
		"y": "a",
		"z": "q",
		" ": " ",
		"\n": "",
	}
	numcases = int(sys.stdin.readline())
	cases = []
	for x in range(0, numcases):
		cases.append(sys.stdin.readline())
		
	#print "Number of Cases:", numcases

	count = 1
	for case in cases:
		astr = ""
		for char in case:
			if char in alphadict:
				astr = astr + alphadict[char]
			else:
				print "[" + char + "]",
		print "Case #%d: %s" % (count, astr)
		count += 1


if __name__ == "__main__":
	runme();

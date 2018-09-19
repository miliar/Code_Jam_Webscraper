"""
	abc-> 1 hit
	>>> searchword(['abc','bca','dac','dbc','cba'],'abc')
	1
	>>> searchword(['abc','bca','dac','dbc','cba'],'(abc)(abc)(abc)')
	3
"""
import re
def searchword(known,testWord):
	count = 0
	testWord = testWord.replace("(","[")
	testWord = testWord.replace(")","]")
	#print testWord
	p = re.compile(testWord)
	for k in known:
		if p.match(k):
			count += 1
	return count

def _test():
	import doctest
	doctest.testmod(verbose=True)

if __name__ == "__main__":
	_test()

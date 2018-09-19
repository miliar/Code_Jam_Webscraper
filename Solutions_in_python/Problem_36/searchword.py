"""
find "wweellccoommee to .." -> "welcome to .."
"""
def print_d(str):
	#print str
	pass

def searchword(input,checkword="welcome to code jam"):
	
	index = [0 for i in range(len(checkword))]
	pos = 0 # position of checkword
	count = 0 # success count for search word
	while True:
		findFlag = False
		matchFlag = False
		c = checkword[pos]
		for p in range( index[pos], len(input) ):
			print_d("compare " + c + " with " + input[p] + " p:" + str(p))
			if c == input[p]:
				print_d("ok")
				# if success for search, count += 1
				if pos >= len(checkword)-1:
					count = (count + 1) % 10000 
					index[pos] = p+1
					matchFlag = True
					print_d("match")
				else:
					print_d( "pos:" + str(pos))
					index[pos]   = p
					index[pos+1] = p+1
					pos += 1
					findFlag = True
				break

		if findFlag == False and matchFlag == False:
			# if don't find, pos -1 and index[pos] += 1
			print_d("return")
			pos -= 1
			index[pos] += 1
			if pos < 0:
				break
	return count

def _test():
	import doctest
	doctest.testmod(verbose=True)

if __name__ == "__main__":
	#print searchword("abbc","abc")
	print searchword("welcome to code jaam") #1
	print searchword("wweellccoommee to code qps jam") #256
	print searchword("welcome to codejam") #0
	print searchword("ewl") #0
	print searchword("wweellccoommee to code qps jjaamm") #2048?



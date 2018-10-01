

cipher = { 'a': 'y', 'b': 'h' , 'c' : 'e' , 'd' : 's', 'e' : 'o' , 'f' : 'c', 'g' : 'v' , 'h' : 'x', 'i' : 'd', 'j' : 'u', 'k' : 'i', 'l' : 'g', 'm' : 'l', 'n' : 'b', 'o' : 'k', 'p' : 'r', 'q' : 'z', 'r' : 't', 's' : 'n', 't' : 'w', 'u' : 'j', 'v' : 'p', 'w' : 'f', 'x' : 'm', 'y' : 'a', 'z' : 'q' , ' ': ' ' }

n = int (raw_input())
for i in range (1, n+1):
	s = raw_input()
	st = ''
	for char in s:
		st = st + cipher[char]
	print "Case #%d: %s"%(i, st)

	
		

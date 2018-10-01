import sys

# letter map
arr = [0]*26;
arr[0]  = 'y'
arr[1]  = 'h'
arr[2]  = 'e'
arr[3]  = 's'
arr[4]  = 'o'
arr[5]  = 'c'
arr[6]  = 'v'
arr[7]  = 'x'
arr[8]  = 'd'
arr[9]  = 'u'
arr[10]  = 'i'
arr[11]  = 'g'
arr[12]  = 'l'
arr[13]  = 'b'
arr[14]  = 'k'
arr[15]  = 'r'
arr[16]  = 'z'
arr[17]  = 't'
arr[18]  = 'n'
arr[19]  = 'w'
arr[20]  = 'j'
arr[21]  = 'p'
arr[22]  = 'f'
arr[23]  = 'm'
arr[24]  = 'a'
arr[25]  = 'q'

f = open(sys.argv[1], "r")
line = f.readline()
line = f.readline()
tc = 1
while (line):
	sys.stdout.write("Case #" + str(tc) + ": ")
	for c in line:
		if(ord(c) >= 97 and ord(c) <= 122):
			sys.stdout.write(arr[ord(str(c))-ord("a")])
		else: 
			sys.stdout.write(c)
	line = f.readline()
	tc += 1

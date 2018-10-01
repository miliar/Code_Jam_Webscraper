import math,sys,os,time

def translate(s):
	t = ''
	for char in s:
		t = t+db[char]	
	return t

file = open(sys.argv[1],'r')

db = {}
db[' '] = ' '
db['a'] = 'y'
db['b'] = 'h'
db['c'] = 'e'
db['d'] = 's'
db['e'] = 'o'
db['f'] = 'c'
db['g'] = 'v'
db['h'] = 'x'
db['i'] = 'd'
db['j'] = 'u'
db['k'] = 'i'
db['l'] = 'g'
db['m'] = 'l'
db['n'] = 'b'
db['o'] = 'k'
db['p'] = 'r'
db['q'] = 'z'
db['r'] = 't'
db['s'] = 'n'
db['t'] = 'w'
db['u'] = 'j'
db['v'] = 'p'
db['w'] = 'f'
db['x'] = 'm'
db['y'] = 'a'
db['z'] = 'q'


for i in range(int(file.readline())):
	print "Case #" + str(i+1) + ":\t" + translate(file.readline().strip('\n'))


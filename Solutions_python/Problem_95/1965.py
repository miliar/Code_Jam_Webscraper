import os

Rep = ['y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q']

fileIN = open('data.in','r')
fileOUT = open('data.out','w')
N = int( fileIN.readline() )

for i in range (1,N + 1):
	res = ''
	for ch in fileIN.readline():
		if ch in Rep:
			res += Rep[ ord(ch) - ord('a') ]
		elif ch == ' ':
			res += ' ' 	
	fileOUT.write('Case #' + str(i) + ': ' +  res + '\n') 

fileOUT.close() 

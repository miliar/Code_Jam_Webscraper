import sys
import os

def convert(inputline):
	outputline = ""
	i = 0 
	for c in inputline:
		i =i + 1
		if(c == 'a'):
			outputline = outputline + 'y'
			continue
		if(c == 'b'):
			outputline = outputline + 'h'
			continue
		if(c == 'c'):
			outputline = outputline + 'e'
			continue
		if(c == 'd'):
			outputline = outputline + 's'
			continue
		if(c == 'e'):
			outputline = outputline + 'o'
			continue
		if(c == 'f'):
			outputline = outputline + 'c'
			continue
		if(c == 'g'):
			outputline = outputline + 'v'
			continue
		if(c == 'h'):
			outputline = outputline + 'x'
			continue
		if(c == 'i'):
			outputline = outputline + 'd'
			continue
		if(c == 'j'):
			outputline = outputline + 'u'
			continue
		if(c == 'k'):
			outputline = outputline + 'i'
			continue
		if(c == 'l'):
			outputline = outputline + 'g'
			continue
		if(c == 'm'):
			outputline = outputline + 'l'
			continue
		if(c == 'n'):
			outputline = outputline + 'b'
			continue
		if(c == 'o'):
			outputline = outputline + 'k'
			continue
		if(c == 'p'):
			outputline = outputline + 'r'
			continue
		if(c == 'q'):
			outputline = outputline + 'z'
			continue
		if(c == 'r'):
			outputline = outputline + 't'
			continue
		if(c == 's'):
			outputline = outputline + 'n'
			continue
		if(c == 't'):
			outputline = outputline + 'w'
			continue
		if(c == 'u'):
			outputline = outputline + 'j'
			continue
		if(c == 'v'):
			outputline = outputline + 'p'
			continue
		if(c == 'w'):
			outputline = outputline + 'f'
			continue
		if(c == 'x'):
			outputline = outputline + 'm'
			continue
		if(c == 'y'):
			outputline = outputline + 'a'
			continue
		if(c == 'z'):
			outputline = outputline + 'q'
			continue
		if(c == ' '):
			outputline = outputline + ' '
			continue
	return outputline

i = 0
f = open("input.in","r")
g = open("output.out","w")
ntestcases = f.readline()

for line in f:
	i = i + 1
	inputline = line
	outputline = "Case #"+str(i)+": "+str(convert(inputline)) +"\n"
	g.write(outputline)

f.close()
g.close()
	

#!/usr/bin/python

rawfile="A-small-attempt1.in"
#rawfile="A-large-practice.in"
ansfile="a"

dict={\
	'a':'y',\
	'b':'h',\
	'c':'e',\
	'd':'s',\
	'e':'o',\
	'f':'c',\
	'g':'v',\
	'h':'x',\
	'i':'d',\
	'j':'u',\
	'k':'i',\
	'l':'g',\
	'm':'l',\
	'n':'b',\
	'o':'k',\
	'p':'r',\
	'q':'z',\
	'r':'t',\
	's':'n',\
	't':'w',\
	'u':'j',\
	'v':'p',\
	'w':'f',\
	'x':'m',\
	'y':'a',\
	'z':'q',\
	' ':' '
}

hf=open(rawfile,'r')
hw=open(ansfile,'w')

line=hf.readline()
line=line.rstrip()
cases=int(line)

for idx in range(1,cases+1):
	line=hf.readline().rstrip()

	hw.write("Case #" + str(idx) + ": ")

	for i in range(0,len(line)):
		hw.write(dict[line[i]])
	hw.write("\n")
	

	

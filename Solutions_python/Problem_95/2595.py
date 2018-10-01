# author : Gayan
# useage : test.py input.in > file.out
import string
import sys
dic = {}
dic['a'] = "y"
dic['b'] = "n"
dic['c'] = "f"
dic['d'] = "i"
dic['e'] = "c"
dic['f'] = "w"
dic['g'] = "l"
dic['h'] = "b"
dic['i'] = "k"
dic['j'] = "u"
dic['k'] = "o"
dic['l'] = "m"
dic['m'] = "x"
dic['n'] = "s"
dic['o'] = "e"
dic['p'] = "v"
dic['q'] = "z"
dic['r'] = "p"
dic['s'] = "d"
dic['t'] = "r"
dic['u'] = "j"
dic['v'] = "g"
dic['w'] = "t"
dic['x'] = "h"
dic['y'] = "a"
dic['z'] = "q"
count = 1
my_dict2 = {} 
for key, val in dic.items():
        my_dict2[val] = key

if(len(sys.argv)>0):
	inputfile = sys.argv[1]
	f = open(inputfile,"r")

#f = open(inputfile,"r")
N = f.readline()
for line in f.readlines():
	line = line.strip()
	out = ""
	for i in line:
		if(i != '' and i != ' '):		
			out = out + str(my_dict2[i])
		else:
			out = out + " "
			
	print "Case #"+str(count)+": "+str(out)
	count = count + 1

f.close()

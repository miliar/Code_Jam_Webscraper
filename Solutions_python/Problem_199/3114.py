import sys
##print sys.argv[1:]
# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

t = int(lines[0])  # read a line with a single integer
##print t

def flip(cake):
	if (cake =="+"):
		return "-"
	else:
		return "+"

def flipcakeAtPos(cakeLine, pos, k):
	if (pos + k) > len(cakeLine):
		return None;
	for inc in range(pos,pos+k,1):
		cakeLine[inc] = flip(cakeLine[inc])
	return cakeLine;

def flipcakes(cakeLine,kFlipper):
	flips = 0;
	for pos, cake in enumerate( cakeLine) :
		if cake =="-":
			cakelineFlipped = flipcakeAtPos(cakeLine,pos,kFlipper)
			flips += 1
			if (cakelineFlipped == None):
				return "impossible"
	return flips;

################# main
f = open(sys.argv[2], 'w')
for index, line in enumerate( lines[1:]) :
	n, m = line.split(" ")  
	results = flipcakes(list(n),int(m))
  	resultsString = "Case #{}: {}".format(index+1, results)
	f.write(resultsString+'\n')
f.close() 
  # check out .format's specification for more formatting options




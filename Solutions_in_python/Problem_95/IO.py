
def readline(file,n):
	f = open(file, 'r')
	i = 0
	for line in f:
		if(i == n):
			f.close() 
			return line
		else:
			i = i + 1
	f.close() 
	return []	


def writeline(file,string):
	f = open(file,'w')
	f.write(string)
	f.close


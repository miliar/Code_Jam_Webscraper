


def get_tidy (a) :
	a_list = map(lambda x : int(x) , list(str(a)))
	for i in xrange (len(a_list)-1):
		while (1):
			for j in xrange (i+1,len(a_list)):
				if a_list[i] > a_list[j] :
					a_list[j-1] -= 1 	
					for k in xrange(j, len(a_list)):
						a_list[k] = 9 
					break
			else: 
				 break 
	return int(''.join(map(lambda x: str(x), a_list)))

if __name__ == '__main__' : 
    # raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    # This is all you need for most Google Code Jam problems.
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
	    	num = int(raw_input())
		result = get_tidy(num)
	    	print "Case #%d: %d"%(i, result )
		         

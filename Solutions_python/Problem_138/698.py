#read off input, 

infile = open("D-large.in", 'r')
op_file = open('output.txt', 'w+')


num_cases = int(infile.readline())

for case_num in range(num_cases):
    t = int(infile.readline())
    naiomi = sorted([float(k) for k in ((infile.readline()).split())])
    ken = sorted([float(k) for k in ((infile.readline()).split())])
    n_low = 0
    n_high = t-1
    k_low = 0
    k_high = t-1
    scores = [0,0]
    for i in range(t):
        # normal war
        if naiomi[n_high] > ken[k_high]:  
	    scores[1] += 1
	    n_high -= 1
	else:
	    n_high -= 1
	    k_high -= 1
	# deceitful war
	if naiomi[n_low] < ken[k_low]:
	    n_low += 1
        else:
	    scores[0] += 1
	    k_low += 1
	    n_low += 1

    op_file.write("Case #"+str(case_num+1)+': '+ str(scores[0])+' '+ str(scores[1])+'\n')

infile.close()
op_file.close() 

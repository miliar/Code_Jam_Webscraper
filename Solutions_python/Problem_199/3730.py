## Open the file with read only permit
f = open('A-large.in')
f_out = open('out.txt', 'w')
## Read the first line 
line = f.readline()

num_input = int(line)
print str(line)
line = f.readline()
case_num = 1

## If the file is not empty keep reading line one at a time
## till the file is empty
while line:
    (cakes_str, k) = line.split()
    print  'line is ' + line
    k = int(k)
    print 'k is' + str(k)
    cake = list(cakes_str)
    flipped = [False] * len(cake)
    flips = 0


    i = 0
    while (i < len(cake)):
    	print 'i is' + str(i)
    	if ((cake[i] == '-' and not flipped[i]) or (cake[i] == '+' and flipped[i])): 
    		if ((len(cake) - i) < k):
    			flips = -1
    			break
    		else:
    			flips = flips + 1
    			print 'flipped len is ' + str(len(flipped))
    			for j in range(i, i + k):
    				print 'j is ' + str(j)
    				flipped[j] = not flipped[j]

    	i = i + 1

    if (flips != -1) :
    	f_out.write('Case #' + str(case_num) + ': ' + str(flips) + '\n')
    else : 
    	f_out.write('Case #' + str(case_num) + ': IMPOSSIBLE' + '\n')

    case_num = case_num + 1	
    line = f.readline()


f.close()
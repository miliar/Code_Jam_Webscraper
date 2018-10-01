import math
f = open('C-small-attempt0.in', 'r')
g = open('output2.txt', 'w')
n = int(f.readline())
count = 0
for i in range (1, n+1):
    lower, upper = [int(x) for x in f.readline().split()]
    m = math.floor(math.sqrt(lower))
    k = m*m
    if k < lower:
        k = (m+1)*(m+1) 
    while k < upper + 1:
        root = math.sqrt(k)
	n1 = root
	rev1 = 0
	while (root > 0):
	    dig = root % 10
	    rev1 = rev1 * 10 + dig
	    root = math.floor(root / 10)
	n2 = k    
	rev2 = 0
	while (k > 0):
	    dig = k % 10
	    rev2 = rev2 * 10 + dig
	    k = math.floor(k / 10)	
        if (n1 == rev1) and (n2 == rev2):
            count = count + 1
        k = (n1+1)*(n1+1)
    line = 'Case #' + str(i) + ': ' + str(count) + '\n'
    g.write(line)      
    count = 0
f.close()
g.close()
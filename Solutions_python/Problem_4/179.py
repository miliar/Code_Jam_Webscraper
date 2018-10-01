import math


def read(filename1, filename2):
    f = open(filename1)
    out = open(filename2, 'w')
    
    cases = int(f.readline())
    
    for i in range(cases):
	
	size = int(f.readline())
	
	l = [[],[]]
	
	for j in range(2):
	    line = f.readline()
	    line = line.split(' ')
	    line = [int(k) for k in line]
	    
	    l[j] = line
	    
	ans = compute(l[0], l[1])
	
	out.write('Case #%d: %d\n' % (i+1, ans)) 
	    
	    
	    
def compute(a1, a2):
    
    a1.sort()
    a2.sort(reverse=True)
    
    ans = 0
    for i in range(len(a1)):
	ans += a1[i]*a2[i]
	
    return ans
    
    
read('A-large.in', 'large-attempt0.out')

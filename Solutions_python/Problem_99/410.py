#!/bin/python




# read the input
f=open("in")
T=int(f.readline())

output=""
for i in xrange(T):
    A,B=tuple(map(int,f.readline().split()))
    p=map(float,f.readline().split())
    stratigies=[]
    ##
    true_percent= reduce(lambda a,b: a*b,p)
    stratigy_if_keep_typing=(B-A+1)*true_percent+(2*B)*(1-true_percent) 
    stratigies.append(stratigy_if_keep_typing)
    ##
    stratigy_if_press_enter=B+2
    stratigies.append(stratigy_if_press_enter)
    ## 
    for bs in xrange(1,A+1):
	stratigy_if_j_backspace=(B-A+1+2*bs)*true_percent
	for j in xrange(0,A):
	    jfalse_percent= reduce(lambda a,b: a*b,p[0:j],1)*(1-p[j])
	    print j,"--", jfalse_percent
	    
	    if j<A-bs:
		stratigy_if_j_backspace+=(2*B-A+2+2*bs)*jfalse_percent
	    else:
		stratigy_if_j_backspace+=(B-A+1+2*bs)*jfalse_percent
	
	stratigies.append(stratigy_if_j_backspace)
    print stratigies
    y=min(stratigies)
    
	
    
    output+="Case #%d: %f\n" %(i+1,y)
    
    
    
    
    
OUTPUT=open("out","w")
OUTPUT.write(output)
print output
print "done"
    
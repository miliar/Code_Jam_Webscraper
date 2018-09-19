T = int(raw_input())
def gcd(a, b):
    if a < b:
    	a,b = b,a
    if a % b == 0:
        return b
    return gcd(b, a % b)
    

def solveCase(N,Pd,Pg):
	if Pd == 0:
		return Pg != 100
	if Pg == 0:
		return Pd == 0
	
	N2 = 100.0/gcd(100,Pd)
	#print N,Pd,Pg
	#print "N2 : %d " % (N2)
	if N < N2:
		return False
	#print "Final ret : %f" % (100.0/gcd(100,Pg))
	#print "100.0/gcd(100,%d)" % (Pg)
	return 100.0/gcd(100,Pg) >= N2
		
for t in range(1,T+1):
	l = map(int,raw_input().split())
	N = l[0]
	Pd = l[1]
	Pg = l[2]
	
	
	y = solveCase(N,Pd,Pg)
	if y:	
		print "Case #%d: %s" % (t,"Possible")
	else:
		print "Case #%d: %s" % (t,"Broken")
	#break
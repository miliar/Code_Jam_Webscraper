import io, sys
#c cookies for farm, 
#p producing
#f add to producing
#x goal
def solve(c,f,x,p):
	#print ("\tSolve - c:{0}, p:{1}, f:{2}, x:{3}".format(c,p,f,x))
	t=0.0
	#if goal with normal production is longer than with 1 farm:
	# - use time to build a farm
	# - increase the production
	while ((x/p) > (c/p + x/(p+f))):
		t+=c/p
		p+=f
	return t + x/p
		
IN = open(sys.argv[1])
for t in range(1, int(IN.readline())+1):
	c, f, x = IN.readline().split()
	print ("Case #{0}: {1:.7f}".format(t, 
			 solve(float(c),float(f),float(x),2.0)))
			 
sys.exit(1)

#example data
IN = io.StringIO("""4
30.0 1.0 2.0
30.0 2.0 100.0
30.50000 3.14159 1999.19990
500.0 4.0 2000.0""")


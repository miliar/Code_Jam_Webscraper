import sys

input = file( sys.argv[1] )

T = int(input.readline())

for case in range(T):
	
	line = input.readline().strip().split(" ")
	N = int(line[0])
	K = int(line[1])
	
	result = (K+1)%(2**N)
	
	output = "Case #%d: %s" % ( case+1, "OFF" if result else "ON" )
	print output
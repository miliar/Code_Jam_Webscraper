import sys

def run():
	if len(sys.argv) != 2:
		print "missing file input path"
		return

	path = sys.argv[1]
	f = open(path, "r")
	output = open("output2", "w+")

	#first line is T
	tests = f.readline()
	tests = tests.split()
	tests = int(tests[0])
	
	for test in range(tests):
		#last one is on or off (1,0)
		result = 0
		
		
		line1 = f.readline()
		line1 = line1.split()
		n = int(line1[0]) # n snappers
		k = int(line1[1]) # k snaps
		result = compute(n,k)
		
		output.write("Case #%d: %s\n" % (test+1, result))
	#end loop through tests
	
	f.close()
	output.close()

def compute(n,k):
#	print "n: %d\nk: %d" % (n,k)
	if n == 1:
		if k % 2 == 0:
#			print "A"
			return "OFF"
		else:
#			print "B"
			return "ON"
	else:
		if n % 2 == 0:
			if k % (2**n) == 2**n-1:
#				print "C"
				return "ON"
			else:
#				print "D"
				return "OFF"
		else:
			if k % (2**n) == 2**n-1:
#				print "E"
				return "ON"
			else:
#				print "F"
				return "OFF"
				
	
if __name__ == "__main__":
	run()
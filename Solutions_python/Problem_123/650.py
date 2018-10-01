def solve(sizes, A, log):
	sizes.sort()
	
	current = A
	count = 0
	
	log.write("current = %d\n" % current)
	log.write(repr(sizes) + '\n')
	
	for i in range(len(sizes)):
		size = sizes[i]
		remove = False
		addcount = 0
		temp = current
		
		if temp <= size:
			while temp <= size:
				if temp - 1 <= 0:
					remove = True
					break
				else:
					log.write("Adding a mote of size %d to %d\n" % (temp - 1, temp))
					temp += (temp - 1)
					addcount += 1
		
			if not remove:
				if addcount < len(sizes) - i:
					remove = False 
					count += addcount
				else:
					remove = True
		
		if not remove:
			current = temp
			current += size
		else:
			log.write("Removing a mote of size %d\n" % (sizes[i]))
			count += 1
	returnvalue = repr(count)
	log.write(returnvalue + '\n')
	return returnvalue

def run(filename):
	f = open(filename + '.in', 'r')
	o = open(filename + '.out', 'w')
	log = open('log.out', 'w')
	for i in range(1, int(f.readline()) + 1):
		A, N = [int(m) for m in f.readline().strip().split(" ")]
		
		sizes = [int(n) for n in f.readline().strip().split(" ")]
		
		outputstring = "Case #%d: %s" % (i, solve(sizes, A, log))
		o.write(outputstring + '\n')
		print outputstring
	log.close()	
	f.close()
	o.close()

run("sample")

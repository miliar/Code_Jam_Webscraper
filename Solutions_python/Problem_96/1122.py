import sys
f = open(sys.argv[1])
in_put = f.readlines()
in_put = in_put[1:]

for i in range(0, len(in_put)):
	data = in_put[i].split(' ')
	data = map(int, data)
	google_n = data[0]
	surprise_n = data[1]
	best_min = data[2]
	to_return = 0
	player = data[3:3+google_n+1]
	for j in xrange(3, len(data)):
		if best_min * 3 <= data[j] + 2:
			to_return += 1
		elif surprise_n > 0 and data[j] > 0:
			if best_min * 3 == data[j] + 3 or best_min *3 == data[j] + 4:
				to_return += 1
				surprise_n -= 1
	print "Case #" +str(i+1)+ ": " + str(to_return)
			
	


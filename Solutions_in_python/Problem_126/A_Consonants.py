#f = open('./ex.txt', 'r')
f = open('./A-small-attempt0.in', 'r')
f_results = open('./result.txt', 'w')

vows = set("aeiou")

cases = int(f.readline())

for case in range(cases):
	line = []
        line = f.readline()
        line = line.split()
        name = line[0]
	n = int(line[1])

#	print name,
#	print n

	nval = 0
	i = 0
	start = -1
	done = -1

	while i != len(name):
#		print "i:" + str(i)
		if name[i] not in vows:
			if start == -1:
				start = i
			if (i - start) == n - 1:
#				print "got a group " + str(start)

				# now count:
				nval = nval + (start - done) * (len(name[start:]) - n + 1)
				done = start
#				print "new nval:" + str(nval)
#				print "new done:" + str(done)

				# continue
				i = start
				start = -1
		else:
#			print "no enough"
			start = -1

		i += 1


	f_results.write("Case #" + str(case + 1) + ": " + str(nval) + "\n")

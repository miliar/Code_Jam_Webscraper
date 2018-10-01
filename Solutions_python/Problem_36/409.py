phrase = "welcome to code jam"

def count(line):
	blah = {}
	for loc in findall('w', line):
		blah[loc] = 1
	for c in phrase[1:]:
		locations = findall(c, line)
		newblah = {}
		for pos in blah:
			for location in locations:
				if location > pos:
					if location in newblah:
						newblah[location] += blah[pos]
					else:
						newblah[location] = blah[pos]
		blah = newblah
	sum = 0
	for key in blah:
		sum += blah[key]
		sum %= 1000
	return sum

def findall(letter, line):
	places = []
	num = 0
	while num < len(line):
		a = line.find(letter, num)
		if a == -1:
			return places
		places.append(a)
		num = a+1
	return places

n = int(raw_input())
for x in xrange(n):
	line = raw_input()
	print "Case #%d: %04d" % (x+1, count(line))	

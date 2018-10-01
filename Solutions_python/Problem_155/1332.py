import pdb
def main():
	f = open('A-large.in')
	result = open('aa-result.txt', 'w')
	testcount = int(f.readline())

	for i in range(testcount):
		#pdb.set_trace()
		lineinput = (f.readline()).split(' ')
		shyness = int(lineinput[0])
		people = lineinput[1]

		friendcount = 0
		total = 0
		for j in range(shyness+1):
			if total < j:
				friendcount += j - total
				total += j - total
			total += int(people[j])
		result.write('Case #%d: %d\n' % (i+1, friendcount))
main()

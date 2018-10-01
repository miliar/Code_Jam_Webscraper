from __future__ import with_statement
import sys
import traceback
import datetime
import psyco
psyco.full()

def readInt(f):
	return int(f.readline().strip())

def buildIndex(s):
	w = "welcome to code jam"

	#quick sanity check, we at least need all the letters in it
	for letter in w:
		if letter not in s:
			return None

	index = []

	last = 0
	dontBother = -1 

	letterIndex = []

	for i in xrange(len(w)):
		if i > 0:
			dontBother = index[i - 1][0]

		letter = w[i]

		try:
			while (True):
				q = s.index(letter, last)
				if q > dontBother:
					#if this is before any letters that are required before it
					#then dont bother with it
					letterIndex.append(q)

				last = q + 1

		except:
			pass
		finally:
			if not letterIndex:
				#not gonna happen
				return []

			index.append(list(letterIndex))
			letterIndex = [] 
			last = 0


	#now we can trim down our index to things that are actually viable
	last = len(s)

	for letterIndex in index[::-1]:
		if letterIndex:
			while letterIndex and letterIndex[-1] > last:
				#if this is after any letters that are required after it
				#then delete it
				del letterIndex[-1]

			if not letterIndex:
				return []

			last = letterIndex[-1]

	return index

def numPositions(q, i, index):
	if i == -1:
		position = -1 
	else:
		position = index[i][q]

	if i == len(index) - 1:
		return 1

	total = 0

	for nextq in xrange(len(index[i + 1])):
		next = index[i + 1][nextq]
		if next > position:
			total += numPositions(nextq, i + 1, index)

	return total % 10000

def solve(s):
	index = buildIndex(s)

	count = 0

	if not index:
		return 0

	return numPositions(0, -1, index)

if __name__ == "__main__":
	start = datetime.datetime.now()
	file = sys.argv[1]
	output = "%s.out" % (file, )

	answers = []

	with open(file) as f:
		cases = readInt(f)

		for case in xrange(cases):
			answers.append(solve(f.readline().strip()))

	i = 0
	with open(output, 'w') as f:
		for answer in answers:
			a = str(answer)
			if len(a) < 4:
				a = "0" * (4 - len(a)) + a
			i += 1
			f.write("Case #%d: %s\n" % (i, a))
			print "Case #%d: %s" % (i, a)

	elapsed = datetime.datetime.now() - start
	print elapsed

import sys

def main():
	data = sys.stdin.read().split("\n")

	nbTest = int(data[0])
	data.pop(0)

	for i in xrange(0, nbTest):
		# each test
		print "Case #%s: %s" % (i+1, sequence(data[0]))
		data.pop(0)

		
def sequence(seq):

	seq = seq.split(" ")
	nbPortal = int(seq[0])
	seq.pop(0)

	posB = 1
	posO = 1
	time = 0
	done = False

	B = [int(seq[x+1]) for x in xrange(0, len(seq)) if seq[x] == 'B']
	O = [int(seq[x+1]) for x in xrange(0, len(seq)) if seq[x] == 'O']

	for i in xrange(0, len(seq), 2):		

		while not done :
			if seq[i] == 'B':
				# blue case
				if posB == B[0]: 
					done = True
					B.pop(0)
				elif posB < B[0] : posB += 1
				else : posB -= 1
				
				if len(O) > 0 and posO < O[0]: posO += 1
				elif len(O) > 0 and posO > O[0] : posO -=1

			elif seq[i] == 'O':
				# orange case
				if posO == O[0]:
					done = True
					O.pop(0)
				elif posO < O[0] : posO += 1
				else : posO -= 1
				
				if len(B) > 0 and posB < B[0]:
					posB += 1		
				elif len(B) > 0 and posB > B[0]:
					posB -=1
		
			time += 1

		done = False
	return time


main()

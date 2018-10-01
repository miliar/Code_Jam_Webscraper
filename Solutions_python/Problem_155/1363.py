import psyco
import sys
import itertools

DEBUG = False

psyco.full()

test_input = r'''4
4 11111
1 09
5 110011
0 1'''.split('\n')


def debug(s):
	if not DEBUG:
		return
	sys.stderr.write(str(s) + '\n')


def readline():
	if DEBUG:
		return test_input.pop(0)
	return raw_input()				
				


def case(casenum):

	m, _, values = readline().partition(' ')
	
	audience = map(int, values)

	standing = 0
	required = 0
	
	for shylevel, n in enumerate(audience):
	
		# If there aren't enough standing...
		if standing < shylevel:
			# Calculate how many are required.
			r = shylevel - standing
			# Add those people.
			standing += r
			# Record them in the total required.
			required += r
			
		# There should always be enough standing now.
		assert(standing >= shylevel)
			
		# There are now enough standing for this level to stand so add them.
		standing += n
	

	output = required
	
	print "Case #%d: %s" % (casenum, output)
	
	

def main():
	numcases = readline()
	for i in xrange(int(numcases)):
		case(i + 1)

main()

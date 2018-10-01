import os
import sys

global num_tests

def powerset(l):
    if len(l) == 1:
        yield l
        yield []
        return
    
    for a in powerset(l[1:]):
        yield [l[0]] + a
        yield a

def flip(strip, i, k):
	to_flip = strip[i:i+k]
	flipped = to_flip.replace('-','f').replace('+','-').replace('f','+')
	return strip[:i] + flipped + strip[i+k:]
def solve(l):
	orig_strip, k = l.split(' ')
	k = int(k)
	flips = 0
	for i in xrange(len(orig_strip) - k + 1):
#		print i, orig_strip, orig_strip[i]
		if orig_strip[i] == '-':
			
			orig_strip = flip(orig_strip, i, k)
			flips += 1
#	print orig_strip
	if orig_strip.count('+') != len(orig_strip):
		return "IMPOSSIBLE"


	return flips

def process_line(l, i):
	if i == 0:
		num_tests = int(i)
	else:
		return solve(l)

def main():

	fn = sys.argv[1]
	fn_out = sys.argv[2]
	lines = open(fn, 'rb').read().splitlines()
	out_fd = open(fn_out, 'wb')
	i = 0
	for line in lines:
		s = process_line(line, i)
		i += 1
		if s is not None:
			out_fd.write('Case #%d: %s' % (i-1, s))
			out_fd.write('\n')

if __name__ == "__main__":
	main()
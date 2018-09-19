import sys
import os

def main(argv=None):
	if argv is None:
		argv = sys.argv
	comp = argv[1]
	prob = argv[2]
	size = argv[3]

	name_in = '%s/data/%s/%s-%s.in' % (os.getcwd(), comp, prob, size)
	name_out = name_in.replace('in', 'out')
	f_in = open(name_in)
	f_out = open(name_out, 'w')
	
	in_lines = f_in.readlines()
	
	solver = __import__('solvers.%s' % comp, fromlist=[''])
	out_lines = getattr(solver, prob.lower())(in_lines)
	for line in out_lines:
		f_out.write("%s\n" % line)
	print 'Success!'
	
if __name__ == '__main__':
	main()
import sys
import math

def is_palindrom(number):
	return str(number) == str(number)[::-1]

def make_work(input='input.txt', output='output.txt'):
    file_in = open(input)
    cases_number = int(file_in.readline().strip())
    for n in xrange(cases_number):
    	case_number = n + 1
    	a, b = map(int, file_in.readline().split(' '))
    	sq_a, sq_b = map(math.sqrt, (a, b)) 
    	sq_a, sq_b = map(int, (math.ceil(sq_a), math.floor(sq_b)))
    	fair_square = 0
    	for x in xrange(sq_a, sq_b + 1):
    		if is_palindrom(x) and is_palindrom(x*x):
    			fair_square += 1    			
        print "Case #%s: %s" % (case_number, fair_square)

if len(sys.argv) >= 2:
    make_work(input=sys.argv[1])
else:
    make_work()

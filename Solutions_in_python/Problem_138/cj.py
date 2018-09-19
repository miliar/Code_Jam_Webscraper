import sys

def ifile():
    filename = sys.argv[1]
    return open(filename, 'r').read()

def parse_cases(input, lines_per_case):
    lines = input.split('\n')
    numcases = lines[0]
    cases = []
    i = 1
    while i < (len(lines) - 1):
        c = lines[i:(i + lines_per_case)]
        cases.append(tuple(c))
        i += lines_per_case
    return cases
	
def get_num_cases(input):
    lines = input.split('\n')
    numcases = lines[0]
    return numcases

def print_answers(answers):
    """Accepts a list of answers. 
            Each answer can be string, or list of integer.
            Prints Case #n: x y z , etc where [x y z] is a list of integers, 
                                            or 'x y z' is a string.
    """
    for case,a in enumerate(answers):
        if isinstance(a, basestring):
            output = a
        else:
            output = ' '.join(str(i) for i in a)
        print 'Case #%s: %s' % (case + 1, output)
        

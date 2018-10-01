'''
Created on April 12, 2014

@author: Lior
'''

INITIAL_COOKIES_PER_SEC = 2.0

def solve(cps, C, F, X):
    time = 0
    while True:
        if X/cps < C/cps+X/(cps+F):
            return time+X/cps
        time += C/cps
        cps += F


def process_files(in_file, out_file):
    num_of_test_cases = int(in_file.next().strip())
    for test_number in xrange(num_of_test_cases):
        C, F, X = tuple(float(i) for i in in_file.next().strip().split(' '))
        result = solve(INITIAL_COOKIES_PER_SEC, C, F, X)
        out_file.write('Case #%d: %s\n' % (test_number+1, result))

if __name__ == '__main__':
    import sys, os
    in_file = sys.argv[1]
    out_file = in_file.replace('.in', '.out')
    with open(in_file, 'rb') as in_file:
        with open(out_file, 'wb') as out_file:
            process_files(in_file, out_file)

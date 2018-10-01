import sys

def memoize(func):
    results = {}
    def wrapper(*args):
        if args not in results:
            results[args] = func(*args)
        return results[args]
    return wrapper

def permutation(items, n=None):
    """
    http://code.activestate.com/recipes/190465/
    >>> list(permutation(range(3)))
    [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]
    >>> list(permutation(range(2, 5)))
    [[2, 3, 4], [2, 4, 3], [3, 2, 4], [3, 4, 2], [4, 2, 3], [4, 3, 2]]
    """
    if n is None:
        n = len(items)
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for cc in permutation(items[:i]+items[i+1:],n-1):
                yield [items[i]]+cc

def bribe(N, order):
    view = [[0, N-1] for _ in xrange(N)]
    #sys.stderr.write('\n%s\n' % view)
    cost = 0
    for prisoner in order:
        first, last = view[prisoner]
	cost += last - first
	for left in xrange(first, prisoner):
            view[left][1] = prisoner-1
	for right in xrange(prisoner+1, last+1):
            view[right][0] = prisoner+1
        #sys.stderr.write('%d -> %s = %d\n' % (prisoner, view, cost))
    return cost

def lowest_bribe(N, release):
    return min(bribe(N, order) for order in permutation(release))

def do_one_test_case(file):
    N, _ = (int(n) for n in file.readline().split())
    release = list(int(b)-1 for b in file.readline().split())
    return lowest_bribe(N, release)

def main(argv):
    f = open(argv[1], 'r')
    cases = int(f.readline().strip())
    sys.stderr.write('Cases: %d\n' % cases)
    output_list = []
    for i in xrange(cases):
        output_list.append('Case #%d: %s\n' % (i+1, do_one_test_case(f)))
        sys.stderr.write('%d of %d done\n' % (i+1, cases))
    f.close()
    if len(argv) > 2:
        expected_f = open(argv[2], 'r')
        expected_list = expected_f.readlines()
        expected_list = [line.strip()+'\n' for line in expected_list[0:-1]]
        if (output_list == expected_list):
            print 'Everything matched!'
        else:
            print 'Actual: %s' % output_list
            print 'Expected: %s' % expected_list
    else:
        print ''.join(output_list)

def test():
    print 'Usage: scriptname.py infile [outfile]'
    print 'I\'ll run the doctests instead!'
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        test()
    else:
        main(sys.argv)

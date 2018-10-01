import sys

def count_options(n, A, B, C, D, x0, y0, M):
    x = x0
    y = y0
    tree_count = \
        [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
    for i in xrange(n):
        x3 = x % 3
        y3 = y % 3
        tree_count[x3][y3] += 1
        x = (A * x + B) % M
        y = (C * y + D) % M
    
    cropcount = 0
    groups = [(x, y) for x in xrange(3) for y in xrange(3)]
    for i in xrange(len(groups)):
        for j in xrange(i, len(groups)):
            for k in xrange(j, len(groups)):
                if i == j and j == k:
                    x3, y3 = groups[i]
                    trees = tree_count[x3][y3]
                    cropcount += trees * (trees - 1) * (trees - 2) / 6
                else:
                    ix3, iy3 = groups[i]
                    jx3, jy3 = groups[j]
                    kx3, ky3 = groups[k]
                    if (((ix3 + jx3 + kx3) % 3 == 0) and 
                        ((iy3 + jy3 + ky3) % 3 == 0)): 
                        itrees = tree_count[ix3][iy3]
                        jtrees = tree_count[jx3][jy3]
                        ktrees = tree_count[kx3][ky3]
                        cropcount += itrees * jtrees * ktrees
    return '%d' % cropcount

def do_one_test_case(file):
    line = [int(n) for n in file.readline().split()]
    n, A, B, C, D, x0, y0, M = line

    return count_options(n, A, B, C, D, x0, y0, M)

def main(argv):
    f = open(argv[1], 'r')
    cases = int(f.readline())
    output_list = []
    for i in xrange(cases):
        output_list.append('Case #%d: %s\n' % (i+1, do_one_test_case(f)))
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

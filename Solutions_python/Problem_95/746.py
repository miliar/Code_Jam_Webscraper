# Reference data
coded = '''ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv y qee'''
decoded = '''our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up a zoo'''

# Data from hint
key = dict(a='y', o='e', z='q')

# Don't change whitespace
key[' '] = ' '
key['\n'] = '\n'

# Use the reference data to generate pairs both ways
key.update(zip(coded, decoded))

if __name__ == '__main__':
    import sys
    fname = sys.argv[1]
    inFile = open(fname, 'r')
    numCases = int(inFile.readline())
    for case in xrange(numCases):
        newstring = ''.join(key[c] for c in inFile.readline())
        print 'Case #%d: %s' % (case+1, newstring),
    inFile.close()

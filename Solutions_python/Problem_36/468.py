# from optparse import OptionParser

# parser = OptionParser()
# parser.add_option("-f", "--file", dest="filename",
#                   help="read input from FILE", metavar="FILE")
# (options, args) = parser.parse_args()

import sys
if len(sys.argv) != 2:
    raise Exception, 'bad number of arguments'

def countmatches(ref, test):
    if len(ref) == 1:
        return test.count(ref)
    elif test.find(ref[0]) == -1:
        return 0
    elif len(ref) == 0:
        return 1
    else:
        firstindex = test.find(ref[0])
        return countmatches(ref[1:], test[firstindex+1:]) + countmatches(ref, test[firstindex+1:])

filename = sys.argv[1]
refstring = "welcome to code jam"
with open(filename) as f:
    N = int(f.readline().strip())
    for i in xrange(N):
        testcase = f.readline().strip()
        count = countmatches(refstring, testcase)
        print "".join(("Case #", str(i+1), ": ", "{0:04}".format(count % 1000)))

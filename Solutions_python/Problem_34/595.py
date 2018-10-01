# from optparse import OptionParser

# parser = OptionParser()
# parser.add_option("-f", "--file", dest="filename",
#                   help="read input from FILE", metavar="FILE")
# (options, args) = parser.parse_args()

import re
import sys
if len(sys.argv) != 2:
    raise Exception, 'bad number of arguments'

filename = sys.argv[1]
with open(filename) as f:
    L, D, N = map(int, f.readline().split(" "))
    words = []
    for i in xrange(D):
        words.append(f.readline().strip())

    for i in xrange(N):
        testcase = f.readline().strip()
        testcase = testcase.replace('(', '[').replace(')', ']')
        testre = re.compile(testcase)
        print "".join((
                "Case #",
                str(i+1),
                ": ",
                str(len(filter(testre.match, words)))))
#     tokens = []
#     while len(testcase) > 0:
#         if testcase[0] == '(':
#             token, testcase = testcase.split(')', 1)
#             token = token[1:]
#             tokens.append(token)
#         else:
#             token = testcase[0]
#             testcase = testcase[1:]
#             tokens.append(token)
#     print tokens

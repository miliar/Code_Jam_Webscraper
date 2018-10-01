# Qualification Round 2015
# Problem D. Ominos
# MichelJ

import sys
import logging
import StringIO
from itertools import *

def echo(fn):
    def wrapped(*v, **k):
        name = fn.__name__
        logging.info( "Called %s(%s)" % (name, ", ".join(map(repr, chain(v, k.values())))) )
        res = fn(*v, **k)
        logging.info( "       %s(%s) returned %s" % (name, ", ".join(map(repr, chain(v, k.values()))),res) )
        return res
    return wrapped

def solve(X, R, C):
    if X==1:
        return "GABRIEL"
    if X==2:
        if (R*C)%2 == 0:
            return "GABRIEL"
        return "RICHARD"
    if X==3:
        if (R*C)%3 == 0:
            if min(R,C)>1:
                return "GABRIEL"
        return "RICHARD"
    if X==4:
        if (R*C)%4 == 0:
            if min(R,C)>2 and max(R,C)>=4:
                return "GABRIEL"
        return "RICHARD"
    return "DON'T KNOW!"
    
def main(data=None):
    if data is not None:
        sys.stdin = StringIO.StringIO(data)
    for tc in xrange(1, int(raw_input()) + 1):
        (X, R, C) = map(int, raw_input().split(' '))
        print 'Case #%d: %s' % (tc, solve(X, R, C))
    if data is not None:
        sys.stdin = sys.__stdin__

sample="""4
2 2 2
2 1 3
4 4 1
3 2 3
"""


# Call main() only if run from command line, not from IDLE
if __name__ == "__main__":
    if True:
#    if '/' not in sys.argv[0] and '\\' not in sys.argv[0]:
        logging.basicConfig(level=logging.ERROR)
        sys.exit(main())
    else:
        logging.basicConfig(level=logging.INFO,format=" %(levelname)s: %(message)s")

import sys
import glob

f = glob.glob('*-%s*.in' % sys.argv[1])[0]

def _tokens(stdin=sys.stdin):
    for line in stdin:
        for token in line.split():
            yield token
        yield StopIteration

_tokens = _tokens(open(f))

def nt(): return next(_tokens)
def ni(): return int(nt())
def nl(): assert nt() is StopIteration
def line(t=str):
    for token in _tokens:
        if token is StopIteration:
            raise StopIteration
        yield t(token)

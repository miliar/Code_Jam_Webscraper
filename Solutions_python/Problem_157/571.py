import sys

mtable = {
    '1': { '1': '1', 'i':  'i', 'j':  'j', 'k':  'k' },
    'i': { '1': 'i', 'i': '-1', 'j':  'k', 'k': '-j' },
    'j': { '1': 'j', 'i': '-k', 'j': '-1', 'k':  'i' },
    'k': { '1': 'k', 'i':  'j', 'j': '-i', 'k': '-1' },
}

def mult(a, b):
    a_s, a_t = a
    b_s, b_t = b
    res = mtable[a_t][b_t]
    if res.startswith('-'):
        a_s = not a_s
    return (a_s ^ b_s, res[-1])

def solve():
    l, x = map(int, sys.stdin.readline().split())
    string = sys.stdin.readline().strip()
    string = string * x
    w = (False, '1')
    sm_i = None
    for i, l in enumerate(string):
        if sm_i is None and w == (False, 'i'):
            sm_i = i
        w = mult(w, (False, l))
    if w != (True, '1'):
        return False
    sm_k = None
    w = (False, '1')
    for i, l in enumerate(string[::-1]):
        if sm_k is None and w == (False, 'k'):
            sm_k = i
        w = mult((False, l), w)
    if sm_i is None or sm_k is None:
        return False
    return (sm_i + sm_k) < len(string)

t = int(sys.stdin.readline())
for i in xrange(1, t+1):
    print 'Case #%d: %s' % (i, 'YES' if solve() else 'NO')


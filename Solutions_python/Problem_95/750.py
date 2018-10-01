mapping = {
    'y': 'a',
    'n': 'b',
    'f': 'c',
    'i': 'd',
    'c': 'e',
    'w': 'f',
    'l': 'g',
    'b': 'h',
    'k': 'i',
    'u': 'j',
    'o': 'k',
    'm': 'l',
    'x': 'm',
    's': 'n',
    'e': 'o',
    'v': 'p',
    'q': 'z',
    'p': 'r',
    'd': 's',
    'r': 't',
    'j': 'u',
    'g': 'v',
    't': 'w',
    'h': 'x',
    'a': 'y',
    'z': 'q',
    ' ': ' '
}
T = int(raw_input())
for i in xrange(T):
    G = raw_input()
    S = ''.join([mapping[c] for c in list(G)])
    print 'Case #%d: %s' % (i+1,S)

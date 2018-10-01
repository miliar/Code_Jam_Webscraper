import sys
rl = sys.stdin.readline
n = int(rl().strip())

rules = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q', 'q':'z'} 

for i in xrange(n):
    line = rl().strip()
    tkn = [ t for t in line ]
    for j in range(len(tkn)):
        tkn[j] = rules[tkn[j]]

    print 'Case #%d: %s' % (i+1, "".join(tkn))


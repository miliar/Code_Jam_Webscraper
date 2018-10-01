import sys
import re

firstline = sys.stdin.readline()

(L, D, N) = map(int, firstline.split())

lex = []
for x in range(D):
    lex.append(sys.stdin.readline())
lex = ''.join(lex)

for (i, pattern) in enumerate(sys.stdin.readlines()):
    pattern = pattern.replace('(','[').replace(')',']')
    matches = re.findall(pattern, lex)
    print 'Case #%d: %d' % (i+1, len(matches))

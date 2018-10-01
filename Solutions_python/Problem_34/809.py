import re
import sys

def solve(words, pattern):
    patsets = []
    pos = 0
    while pos < len(pattern):
        s = set()
        if pattern[pos] == '(':
            pos += 1
            while pattern[pos] != ')':
                s.add(pattern[pos])
                pos += 1
        else:
            s.add(pattern[pos])
        pos+=1
        patsets.append(s)
    res = 0
    for word in words:
        ok = 1
        for (i, let) in enumerate(word):
            if let not in patsets[i]:
                ok = 0
                break
        if ok: res+=1
    return res

f = file(sys.argv[1])
out = open("out.txt", 'w')
(L, D, N) = [int(n) for n in f.readline().split(" ")]
words = []
for i in xrange(0, D):
    words.append(f.readline().rstrip())
for i in xrange(0, N):
    pattern = f.readline().rstrip()
    out.write("Case #{0}: {1}\n".format(i+1, solve(words, pattern)))
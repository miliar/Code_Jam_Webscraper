import sys
from collections import Counter
import operator



def istidy(s):
    for i in range(1, len(s)):
        if s[i-1]>s[i]: return False
    return True

def lower(s):
    borrow = False
    for i in range(len(s)-1, -1, -1):
        if borrow: s[i] = s[i] - 1
        if istidy(s[0: i+1]): return s
        borrow = s[i]!=9
        s[i] = 9
    return s


convert = lambda s: list(map(int, list(s)))
    


fin = sys.stdin
fout = sys.stdout
ferr = sys.stderr

T = int(fin.readline())

for t in range(T):
    s = fin.readline().strip()
    s = convert(s)
    s = lower(s)
    s = "".join(map(str, s)).lstrip("0")
    fout.write("Case #%i: %s\n" % (t+1, s))


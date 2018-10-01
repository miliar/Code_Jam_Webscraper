import sys;
import re;

MAX_ALT = 10000;

def solve(s, rest):
    if len(rest) == 0:
        return 1;
    elif len(s) == 0 or s[0] != rest[0]: 
        return 0;

    s = s[1:]
    rest = rest[1:]

    if len(rest) == 0:
        return 1;

    result = 0;
    for i in xrange(len(s)):
        result += solve(s[i:], rest);

    return result;

out = open(sys.argv[2], "w");
f = open(sys.argv[1]);
N = int(f.readline());

for i in xrange(N):
    str = f.readline().strip();
    result = solve(" " + str, " welcome to code jam");
    out.write("Case #%d: %04d\n" % (i+1, result));

out.close();

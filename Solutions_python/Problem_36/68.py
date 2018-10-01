import sys

text = "welcome to code jam"
def f(c, i, p):
    if text[i] == c:
        return p
    return 0

for cas in range(int(sys.stdin.readline())):
    s = sys.stdin.readline()
    a = [1] + [0] * 19
    for i in range(len(s)):
        a = [1] + [(a[j + 1] + f(s[i], j, a[j])) % 10000 for j in range(19)]
    print "Case #%d: %04d" % (cas + 1, a[19])

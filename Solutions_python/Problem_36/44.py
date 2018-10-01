data = {}
pattern = 'welcome to code jam'
def f(line, pattern):
    if (line, pattern) not in data:
        if len(pattern) == 1:
            data[line, pattern] = line.count(pattern)
        else:
            data[line, pattern] = sum(f(line[x + 1:], pattern[1:]) for x in xrange(0, len(line) - 1) if line[x] == pattern[0])
    return data[line, pattern]
n = int(raw_input())
for x in xrange(1, n + 1):
    line = raw_input()
    print 'Case #%d: %s' % (x, ('%04d' % f(line, pattern))[-4:])

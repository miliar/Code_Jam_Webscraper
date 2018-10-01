def parse(s):
    l = []
    while True:
        if not s:
            return l
        if s[0] == '(':
            pos = s.find(')')
            l.append(s[1:pos])
            s = s[pos+1:]
        else:
            l.append(s[0])
            s = s[1:]
    
import sys
import itertools

lines = sys.stdin.readlines()
allwords = []
l, d, n = map(int, lines[0].split(' '))
for word in lines[1:d+1]:
    allwords.append(word)

i = 1
for test in lines[d+1:]:
    l = parse(test)
    count = 0
    for word in allwords:
        if all(letter in poss for letter, poss in itertools.izip(word, l)):
            count += 1
    print "Case #%d: %d" % (i, count)
    i += 1

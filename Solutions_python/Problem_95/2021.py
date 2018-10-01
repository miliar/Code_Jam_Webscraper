import string

#s = ["ejp mysljylc kd kxveddknmc re jsicpdrysi", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "de kr kd eoya kw aej tysr re ujdr lkgc jv", "q", "z"]
#a = ["our language is impossible to understand", "there are twenty six factorial possibilities", "so it is okay if you want to just give up", "z", "q"]

d = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}

t = int(raw_input())

for i in xrange(t):
    n = raw_input()
    test = map(lambda x: d[x], n)
    test = "".join(test)
    print 'Case #%d:' % (i+1), test

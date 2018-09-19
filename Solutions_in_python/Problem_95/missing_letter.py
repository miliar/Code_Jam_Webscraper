inp = raw_input("gimmeh alphabet: ")

d = [chr(ord('a') + i) for i in xrange(26)]

for x in inp:
    if x in d:
        d.remove(x)

print d[0]

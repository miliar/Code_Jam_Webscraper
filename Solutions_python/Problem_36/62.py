from sys import stdin
n = int(stdin.readline().strip())

magic="welcome to code jam"
cc=1
for line in stdin:
    line = line.strip()
    o = [1 for _ in xrange(len(line)+1)]
    for c in magic:
        n = [0 for _ in xrange(len(line)+1)]
        for i in xrange(len(line)):
            n[i+1] = n[i]
            if c == line[i]: n[i+1] = (n[i+1] + o[i])%10000
        o = n
    print "Case #%d: %04d"%(cc,n[-1])
    cc += 1

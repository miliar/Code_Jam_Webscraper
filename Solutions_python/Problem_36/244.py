import sys
n = int(sys.stdin.readline().strip())
phrase = "maj edoc ot emoclew"
for i in range(n):
    line = list(sys.stdin.readline().strip())
    line.reverse()
    line = "".join(line)
    cache = [[0 for j in range(len(phrase))] for k in range(len(line))]
    for j, c1 in enumerate(line):
        if c1 == "m":
            cache[j][0] = 1
        for k, c2 in enumerate(phrase):
            if c1 != c2: continue
            for l in range(j):
                cache[j][k] = (cache[j][k] + cache[l][k-1]) % 10000
    print "Case #%d: %04d" % (i + 1, sum(cache[j][-1] for j in range(len(line))))

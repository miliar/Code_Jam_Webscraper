# Mallin Moolman

filename = "A-small-attempt0.in"
f = open (filename)
outfile = open (filename.rsplit(".", 1)[0] + ".out", 'w')

n = int(f.readline().strip())

for i in xrange(n):
    line = f.readline().strip()
    base = len(set(list(line)))
    if base == 1:
        base = 2
    final = ['1']
    lookup = {line[0]:'1'}
    next = [0] + range(2, base)
    next.reverse()
    next = [str(x) for x in next]
    for char in line[1:]:
        if char in lookup.keys():
            final.append(lookup[char])
        else:
            d = next.pop()
            lookup[char] = d
            final.append(d)

              
    out = int("".join(final), base)
    outfile.write("Case #%d: %d\n" % (i+1, out))
            

f.close()
outfile.close()

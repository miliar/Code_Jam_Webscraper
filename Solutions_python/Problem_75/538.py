
def invoke(line):
    parts = line.strip().split(' ')
    pairs = {}
    oppos = {}
    c = int(parts[0])
    for i in range(c):
        s = parts[i+1]
        pairs[(s[0],s[1])] = s[2]
        pairs[(s[1],s[0])] = s[2]
    d = int(parts[1+c])
    for i in range(d):
        s = parts[i+2+c]
        oppos[s[0]] = s[1]
        oppos[s[1]] = s[0]
    seq = parts[-1]
    results = []
    for e in seq:
        results.append(e)
        while len(results) >= 2:
            a = results[-1]
            b = results[-2]
            if pairs.has_key((a, b)):
                results = results[:-2]
                results.append(pairs[(a,b)])
                continue
            if oppos.has_key(a):
                if oppos[a] in results:
                    results = []
            break
    return results

with open('B-small-attempt0.in', 'r') as f:
    line = f.readline()
    t = int(line)
    for i in range(t):
        line = f.readline()
        elements = invoke(line)
        print 'Case #%d: [%s]' % (i + 1, ', '.join(elements))

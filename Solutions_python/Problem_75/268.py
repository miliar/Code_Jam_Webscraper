import sys

file_prefix = sys.argv[1]
with open(file_prefix + '.in', 'r') as f_in:
    t = int(f_in.readline())
    with open(file_prefix + '.out', 'w') as f_out: 
        for i in xrange(t):
            x = f_in.readline().strip().split(' ')
            c, o = dict(), dict()
            for j in xrange(int(x.pop(0))):
                t = x.pop(0)
                c[(t[0], t[1])] = c[(t[1], t[0])] = t[2]
            for j in xrange(int(x.pop(0))):
                t = x.pop(0)
                o[t[0]] = t[1]
                o[t[1]] = t[0]

            t = []
            for j in x.pop():
                t.append(j)
                while len(t) >= 2 and (t[-2], t[-1]) in c: 
                    t[-2:] = c[(t[-2], t[-1])]
                if t[-1] in o and o[t[-1]] in t:
                    t = []
            f_out.write('Case #%s: [%s]\n' % (i + 1, ', '.join(t)))
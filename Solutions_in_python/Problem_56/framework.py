"""
Framework for Google code jam
  (c) 2010, Nicolas Dumazet <nicdumz@gmail.com>

Released under WTFPL, have fun with it.
"""
import sys
import itertools

fin = fout = None
try:
    fname = sys.argv[1]
    fin = open(fname, 'r')
    fout = open("%s.out" % fname.split(".")[0], 'w')
except IndexError:
    raise ValueError("Please give a filename on commandline")

def mint(line):
    return map(int, line.split())
def mfloat(line):
    return map(float, line.split())

class Solver(object):
    def __init__(self, lines_per_problem=1):
        self.n = lines_per_problem
        self.lines = fin
        self.size = int(self.lines.next())
        self.problem = 0

    def __iter__(self):
        return self

    def next(self):
        """List of lines for each problem"""
        l = list(itertools.islice(self.lines, self.n))
        if not l:
            raise StopIteration
        n, k = mint(l[0])
        l = list(itertools.islice(self.lines, n))
        return n, k, l

    def answer(self, answer):
        """Answer current problem"""
        self.problem += 1
        if not isinstance(answer, (list, tuple)):
            answer = [answer]
        s = "Case #%d: %s" % (self.problem, " ".join(map(str, answer)))
        print >> fout, s
        print >> sys.stderr, s

    def check_size(self):
        assert self.problem == self.size, \
                "not answered all problems? (answered:%s, size:%s)" \
                % (self.problem, self.size)



s = Solver(1)
def ans(blue, red):
    if blue and red:
        return 
for x in s:
    n, k, lines = x
    lines = map(lambda x: list(x.strip().replace(".", "")), lines)
    def extend(l):
        d = n - len(l)
        if d > 0:
            return list('.'*d) + l
        return l
    lines = map(extend, lines)

    blue = red = False
    b = 'B' * k
    r = 'R' * k
    for l in lines:
        j = ''.join(l)
        #print j
        if not blue and b in j:
            blue = True
        if not red and r in j:
            red = True
        if blue and red:
            break
    if blue and red:
        s.answer('Both')
        continue

    cols = [''.join(l[i] for l in lines) for i in range(n)]
    for l in cols:
        #print l
        if not blue and b in l:
            blue = True
        if not red and r in l:
            red = True
        if blue and red:
            break
    if blue and red:
        s.answer('Both')
        continue

    diags = []
    def do():
        global blue, red
        for i in range(n-k+1):
            for j in range(n-k+1):
                l = ''.join(lines[i+d][j+d] for d in range(k))
                #print l
                if not blue and b in l:
                    blue = True
                if not red and r in l:
                    red = True
                if blue and red:
                    return
                l = ''.join(lines[n-i-1-d][j+d] for d in range(k))
                #print l
                if not blue and b in l:
                    blue = True
                if not red and r in l:
                    red = True
                if blue and red:
                    return
    
    do()
    if blue and red:
        s.answer('Both')
    elif blue:
        s.answer('Blue')
    elif red:
        s.answer('Red')
    else:
        s.answer('Neither')

s.check_size()

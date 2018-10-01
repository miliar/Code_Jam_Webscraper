#!/usr/bin/env python

FNAME = "A-large.in"

class Case(object):
    def __init__(self, p, k, l, freqs):
        self.p = p
        self.k = k
        self.l = l
        self.freqs = sorted(freqs)
        self.freqs.reverse()

def getmin(p, k, l, freqs):
    s = 0
    pos = 1
    keypos = 1
    for freq in freqs:
        if keypos > k:
            keypos = 1
            pos += 1
            if pos > p:
                return "Impossible"
        s += pos * freq
        keypos += 1
    return str(s)
    
def parse(lines):
    cases = []
    i = 1
    while i < len(lines):
        ints = map(int, lines[i].split())
        p, k, l = ints
        i += 1
        freqs = map(int, lines[i].split())
        cases.append( Case(p, k, l, freqs) )
        i += 1
    return cases

if __name__ == "__main__":
    lines = file(FNAME).read().splitlines()
    answers = [getmin(case.p, case.k, case.l, case.freqs) for case in parse(lines)]
    outlines = ["Case #%d: %s\n" % (i + 1, answer) for i, answer in enumerate(answers)]
    file(FNAME + ".out", "w").writelines(outlines)


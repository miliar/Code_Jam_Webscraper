# -*- coding: utf-8 -*-

T = int(raw_input())
for case in xrange(1, T + 1):
    data = raw_input().split(' ')
    C = int(data.pop(0))
    CL = data[:C]  # like "QFT", indicates "QF" => "T" and "FQ" => "T"
    data = data[C:]
    D = int(data.pop(0))
    DL = data[:D]  # like "QF", opposed each other.
    data = data[D:]
    N = int(data.pop(0))
    Q = data.pop(0)
    assert len(data) == 0

    def consists(a, b, c):
        return a + b == c or b + a == c

    def is_combi(a, b):
        for comb in CL:
            if consists(a, b, comb[:2]):
                return comb[2]
        return False

    def is_opposed(a, b):
        for opp in DL:
            if consists(a, b, opp):
                return True
        return False

    current = ''
    for c in Q:
        # Check combination.
        if 0 < len(current):
            r = is_combi(current[-1], c)
            if r:
                current = current[:-1]
                current += r
                continue
        # Check opposed.
        for bi in xrange(len(current)):
            if is_opposed(current[-1 - bi], c):
                current = ''
                break
        else:
            current += c
    print 'Case #%d: [%s]' % (case, ', '.join(c for c in current))

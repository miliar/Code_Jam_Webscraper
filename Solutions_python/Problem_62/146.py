import sys


name = "A-large"


class Fakeout(object):
    def __init__(self, stdout, fout):
        self.stdout = stdout
        self.fout = fout

    def write(self, s):
        self.stdout.write(s)
        self.stdout.flush()
        self.fout.write(s)
        self.fout.flush()

sys.stdin = open(name + ".in")
sys.stdout = Fakeout(sys.stdout, open(name + ".out", "w"))


##############

n_cases = input()

for case_number in xrange(1, n_cases + 1):
    n_wires = input()
    wires = []
    for wire in xrange(n_wires):
        wires.append(map(int, raw_input().split()))

    inters = 0

    for n, (a1, b1) in enumerate(wires):
        for a2, b2 in wires[n+1:]:
#            print a1, b1, ":", a2, b2
            if a1 > a2:
                if b1 < b2:
                    inters += 1
            else:
                if b1 > b2:
                    inters += 1

    print "Case #%d:"%case_number, inters

# python 2.7

import os, sys

class Input:
    def __init__(self, fp): self.fp = fp
    def m(self, n, t=str):  return [map(t, list(self.line())) for i in range(n)]
    def ms(self, n, t=str, sep=' '):  return [map(t, self.line().split(sep)) for i in range(n)]
    def line(self):  return self.fp.readline().strip()
    def lines(self, n): return [self.fp.readline().strip() for x in range(n)]
    def words(self): return self.line().split()
    def int(self):   return int(self.line())
    def ints(self):  return map(int, self.words())
    def float(self): return float(self.line())
    def floats(self):return map(float, self.words())
    def str(self):   return self.line()
    def types(self, *types): return [t(w) for t,w in zip(types, self.words())]

if __name__ == "__main__":

    fn = "test.txt" if len(sys.argv) <= 1 else sys.argv[1]
    f = Input(open(fn))
    fout = open(os.path.splitext(fn)[0] + ".out", "w")

    def answer(t, ans):
        o = "Case #%d: %s\n"%(t, ans)
        sys.stdout.write(o)
        fout.write(o)

    for case in range(f.int()):
        A, B, K = f.ints()

        count = 0
        for a in range(A):
            for b in range(B):
                if a & b < K: count += 1

        answer(case + 1, count)

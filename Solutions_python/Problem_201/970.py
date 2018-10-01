from sys import stdin, stdout

T = int(stdin.readline().strip())

class Tree:
    def __init__(self, W):
        self.O = False
        self.W = W
        self.l = None
        self.r = None

    def take_a_seat(self):
        if self.O:
            if self.l.W >= self.r.W:
                self.W = max(self.l.take_a_seat(), self.r.W)
            else:
                self.W = max(self.l.W, self.r.take_a_seat())
            return self.W
        else:
            self.l = Tree((self.W-1)//2)
            self.r = Tree(self.W//2)
            self.O = True
            self.W = max(self.l.W, self.r.W)
            return self.W

for case_num in range(1, T+1):
    N,K = map(int, stdin.readline().strip().split())
    root = Tree(N)
    for i in range(K-1):
        root.take_a_seat()
    hi = max((root.W-1)//2, root.W//2)
    lo = min((root.W-1)//2, root.W//2)
    stdout.write("Case #{:d}: {:d} {:d}\n".format(case_num, hi, lo))

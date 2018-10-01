class Solver(object):
    def run(self):
        self.T = int(input())
        for case in range(self.T):
            row, K = input().split(' ')
            self.K = int(K)
            self.row = [1 if char == '+' else 0 for char in row]
            self.n = len(self.row)
            idx = 0
            flips = 0
            for i in range(len(self.row)):
                if self.row[i] == 0:
                    idx = i
                    break
            possible = True
            while sum(self.row) < self.n:
                if not self.flip(idx):
                    possible = False
                    break
                else:
                    for i in range(idx, self.n):
                        if self.row[i] == 0:
                            idx = i
                            break
                    flips += 1
            print('Case #%d: %s' % (case + 1, flips if possible else 'IMPOSSIBLE'))

    def flip(self, idx):
        if idx > self.n - self.K:
            return False
        else:
            for i in range(idx, idx + self.K):
                self.row[i] = 1 - self.row[i]
            return True

Solver().run()

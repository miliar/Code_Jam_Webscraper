from __future__ import print_function


class Template:
    def __init__(self):
        self.cout = True

    def process(self):
        self.D, self.N = [int(x) for x in self.fin.readline().strip().split()]
        self.H = [self.fin.readline().strip().split() for _ in range(self.N)]
        self.T = []
        self.S = []
#         self.print_tmp(self.H)
        for i in range(self.N):
            self.cal_time(i)
#         self.print_tmp(self.T)
        for i in range(self.N):
            self.cal_speed(i)
        self.print_tmp(self.S)
        ans = sorted(self.S)[0]

        self.print_ans(ans)

    def cal_time(self, i):
        k, s = [int(x) for x in self.H[i]]
        self.T.append(float((self.D - k) / float(s)))

    def cal_speed(self, i):
        self.S.append(float(self.D / self.T[i]))

    def solve(self):
        self.fin = open('../in.in', 'r')
        # fin = open('../test', 'r')
#         self.fin = open('../example.txt', 'r')
        self.fout = open('../out', 'w')
        times = int(self.fin.readline())
        for i in range(times):
            self.print_ans('Case #%d: ' % (i + 1))
            self.process()
            self.print_ans('\n')
        self.fin.close()
        self.fout.close()
        print('Done!')

    def make_test(self):
        fout = open('../test', 'w')
        fout.write('1\n2000\n')
        for i in range(2000):
            fout.write('%d %d\n' % ((-1000 + i), 1000 - i))
        fout.close()

    def print_tmp(self, s):
        if self.cout:
            print(str(s))

    def print_ans(self, s):
        self.fout.write(str(s))
        if self.cout:
            print(str(s), end='')


def nC2(n):
    return int(n * (n - 1) / 2)


def line(a, b):
    return pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2)


if __name__ == '__main__':
    t = Template()
    t.solve()

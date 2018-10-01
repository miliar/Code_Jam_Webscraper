from sys import stdin, stdout
import math

class Solver :

    def run(self, caseIndex) :
        self.input()
        self.calculate()
        self.output(caseIndex)

    def input(self) :
        self.N, self.K = (int(_) for _ in stdin.readline().split())
        self.U = float(stdin.readline())
        self.P = list(float(_) for _ in stdin.readline().split())

    def calculate(self) :
        self.P.sort()
        while self.U > 0 :
            index = self.N
            for i in range(self.N) :
                if self.P[i] != self.P[0] :
                    index = i
                    break

            if index == self.N :
                h = 1.0
            else :
                h = self.P[index]

            if index * (h - self.P[0]) > self.U :
                extra = self.U / index
                for i in range(index) :
                    self.P[i] += extra
                self.U = 0.0
            else :
                self.U -= index * (h - self.P[0])
                for i in range(index) :
                    self.P[i] = h

            if h == 1.0 :
                break

        self.result = 1.0
        for i in range(self.N) :
            self.result *= self.P[i]

    def output(self, caseIndex) :
        stdout.write("Case #%d: %.9f\n" % (caseIndex, self.result))

if __name__ == "__main__" :
    caseNum = int(stdin.readline())
    for caseIndex in range(1, caseNum + 1) :
        instance = Solver()
        instance.run(caseIndex)


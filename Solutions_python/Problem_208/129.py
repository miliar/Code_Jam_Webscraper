from sys import stdin, stdout
import math

class Solver :

    def run(self, caseIndex) :
        self.input()
        self.calculate()
        self.output(caseIndex)

    def input(self) :
        self.N, self.Q = (int(_) for _ in stdin.readline().split())

        self.horse = []
        for i in range(self.N) :
            self.horse.append([float(_) for _ in stdin.readline().split()])

        self.distance = []
        for i in range(self.N) :
            d = [float(_) for _ in stdin.readline().split()]
            self.distance.append(d)

        self.query = []
        for i in range(self.Q) :
            self.query.append((int(_) - 1 for _ in stdin.readline().split()))

    def calculate(self) :
        self.time = []
        for i in range(self.N) :
            self.time.append(self.distance[i][:])
        self.floyd(self.time)

        for i in range(self.N) :
            for j in range(self.N) :
                if self.time[i][j] > 0 :
                    if self.time[i][j] > self.horse[i][0] :
                        self.time[i][j] = -1
                    else :
                        self.time[i][j] /= self.horse[i][1]

        self.travel = []
        for i in range(self.N) :
            self.travel.append(self.time[i][:])
        self.floyd(self.travel)

        self.result = []
        for i, j in self.query :
            self.result.append(self.travel[i][j])
    
    def floyd(self, d) :
        for i in range(self.N) :
            for x in range(self.N) :
                for y in range(self.N) :
                    if d[x][i] >= 0 and d[i][y] >= 0 :
                        if d[x][y] < 0 or d[x][y] > d[x][i] + d[i][y] :
                            d[x][y] = d[x][i] + d[i][y]

    def output(self, caseIndex) :
        stdout.write("Case #%d:" % caseIndex)
        for t in self.result :
            stdout.write(" %.8f" % t)
        stdout.write("\n")

if __name__ == "__main__" :
    caseNum = int(stdin.readline())
    for caseIndex in range(1, caseNum + 1) :
        instance = Solver()
        instance.run(caseIndex)


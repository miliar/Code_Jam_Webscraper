# https://code.google.com/codejam/contest/2974486/dashboard

class Game(object):
    def __init__(self, farmCost, farmRate, target):
        self.farmCost = farmCost
        self.farmRate = farmRate
        self.target = target
        self.rate = 2.0
        self.cookies = 0.0
        self.time = 0.0

    def completeAtCurrent(self):
        remaining = self.target - self.cookies
        return self.time + (remaining / self.rate)

    def nextFarmTime(self):
        return self.time + self.farmCost / self.rate

    def completeAtNext(self):
        rate = self.rate + self.farmRate
        return self.nextFarmTime() + (self.target / rate)
        

    def solve(self):
        cc = self.completeAtCurrent()
        cn = self.completeAtNext()
        while cc > cn:
            self.time = self.nextFarmTime()
            self.rate += self.farmRate
            cc = cn
            cn = self.completeAtNext()
        return cc
        

if __name__ == '__main__':
    fp = open('B-large.in')
    ap = open('answer.txt', 'w')
    tests = int(fp.readline())
    for i in range(tests):
        line = fp.readline()
        g = Game(*[float(p) for p in line.strip().split(' ')])
        msg = "Case #%d: %0.7f\n" % (i+1, g.solve())
        ap.write(msg)
    fp.close()
    ap.close()

    

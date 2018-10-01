class Game:
    def __init__(self, c, f, x):
        self.c = c # farm price
        self.f = f # farm rate
        self.x = x # target
        self.rate = 2.0
        self.time = 0.0
        self.notDone = True
    def advance(self):
        if self.notDone:
            timeNoFarm = self.x/self.rate
            timeWithFarm = self.c/self.rate + self.x/(self.rate + self.f)
            if timeNoFarm < timeWithFarm:
                self.time += timeNoFarm
                self.notDone = False
            else:
                self.time += self.c/self.rate
                self.rate += self.f
    def solve(self):
        while self.notDone:
            self.advance()
        return self.time

f = file('b.in', 'r')
lines = f.readlines()
games = int(lines[0])
cons = [map(float, l.split()) for l in lines[1:]]

g = file('b.out', 'w')

g.writelines(["Case #{}: {}\n".format(i+1, round(Game(cons[i][0], cons[i][1], cons[i][2]).solve(), 8)) for i in xrange(games)])

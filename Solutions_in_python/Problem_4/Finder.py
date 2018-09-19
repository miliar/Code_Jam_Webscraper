#Finder.py

class Finder:
    def __init__(self, x, y):
        self.x = x;
        self.y = y;

    def getMinScalar(self):
        self.x.sort()
        self.y.sort()

        self.xIndex = len(self.x)
        for index in range(len(self.x)):
            if self.x[index] > 0:
                self.xIndex = index
                break

        self.yIndex = len(self.y)
        for index in range(len(self.y)):
            if self.y[index] > 0:
                self.yIndex = index
                break

        self.x = self.x[:self.xIndex] + sorted(self.x[self.xIndex:])
        self.y = sorted(self.y[self.yIndex:],reverse=True) + sorted(self.y[:self.yIndex],reverse=True) 

        print self.x
        print self.y

        minScalar = sum([self.x[index]*self.y[index] for index in range(len(self.x))])
        return minScalar

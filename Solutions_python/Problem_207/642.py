class TestCase():
    def __init__(self, stablecount, r, o, y, g, b, v):
        self.stablecount = stablecount
        self.r = r
        self.o = o
        self.y = y
        self.g = g
        self.b = b
        self.v = v
        self.stables = ["+" for i in range(self.stablecount)]
        self.next = 0

        
        self.possibleB = []
        self.possibleG = []
        self.possibleY = []
    def placeNext(self, color):
        self.stables[self.next] = color
        self.next +=2
        if self.next >= self.stablecount:
            self.next = 1

    def verify(self):
        for i in range(self.stablecount):
            if self.stables[i] == "+":
                return False
            if self.stables[i]==self.stables[i-1]:
                return False
        #if self.stables[0] == self.stables[-1]:
         #   return False
        rcount = 0
        ycount = 0
        bcount = 0
        for s in self.stables:
            if s== "R":
                rcount+=1
            elif s== "Y":
                ycount+=1
            elif s== "B":
                bcount+=1
        if rcount != self.r:
            print("Error: r")
            return False
        if bcount != self.b:
            print("Error: b")
            return False
        if ycount != self.y:
            print("Error: y")
            return False
        return True


    def solve(self):

        if self.b == max(self.r, self.b, self.y):
            for i in range(self.b):
                self.placeNext("B")
            if self.r == max(self.r, self.y):
                for i in range(self.r):
                    self.placeNext("R")
                for i in range(self.y):
                    self.placeNext("Y")
            elif self.y == max(self.r, self.y):
                for i in range(self.y):
                    self.placeNext("Y")
                for i in range(self.r):
                    self.placeNext("R")
        elif self.r == max(self.r, self.b, self.y):
            for i in range(self.r):
                self.placeNext("R")
            if self.b == max(self.b, self.y):
                for i in range(self.b):
                    self.placeNext("B")
                for i in range(self.y):
                    self.placeNext("Y")
            elif self.y == max(self.b, self.y):
                for i in range(self.y):
                    self.placeNext("Y")
                for i in range(self.b):
                    self.placeNext("B")
        else:
            for i in range(self.y):
                self.placeNext("Y")
            if self.b == max(self.b, self.r):
                for i in range(self.b):
                    self.placeNext("B")
                for i in range(self.r):
                    self.placeNext("R")
            elif self.r == max(self.b, self.r):
                for i in range(self.r):
                    self.placeNext("R")
                for i in range(self.b):
                    self.placeNext("B")

                    
        if self.verify():
            return "".join(self.stables)
        else:
            return "IMPOSSIBLE"# + "".join(self.stables)
            

            


def loadTestCases(taskChar, path):
    out = []
    input_file = open(path)
    for i in range(int(input_file.readline())):
        tmp = [int(i) for i in input_file.readline().split()]
        (stablecount, r, o, y, g, b, v) = tmp
        print(tmp)
        out.append(TestCase(stablecount, r, o, y, g, b, v))
    input_file.close()
    return out

def solve(path):
    tcs = loadTestCases("B", path)
    output_file = open(path[:-3]+".out", "w")
    count = 1
    for t in tcs:
        output_file.write("Case #"+str(count)+": "+str(t.solve())+"\n")
        print(("Case #"+str(count)))
        count += 1
        
    output_file.close()

        
        
solve("B-small-attempt3.in")

    

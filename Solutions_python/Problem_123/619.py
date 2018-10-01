import os
import sys

class ConsumedAllException(Exception):
    pass

class Game:
    
    def __init__(self, A, motes, cost=0):
        self.A = A
        self.motes = motes
        self.cost = cost
        
    def eatNext(self):
        if not self.motes:
            raise ConsumedAllException()
        if self.A == 1:
            self.cost = len(self.motes)
            raise ConsumedAllException()
        if self.A > self.motes[0]:
            self.A += self.motes[0]
            self.motes.pop(0)
        else:
            if self.motes[0] == 1:
                self.cost = len(self.motes)
                raise ConsumedAllException()
            
            motes2 = self.motes[1:]
            motes3 = [self.A-1] + self.motes
            self.cost += 1
            
            cost1 = Game(self.A, motes2, cost=self.cost).solve()
            cost2 = Game(self.A, motes3, cost=self.cost).solve()
            
            self.cost = min(cost1, cost2)
            raise ConsumedAllException()
        
    def solve(self):
        try:
            while True:
                self.eatNext()
        except ConsumedAllException as e:
            return self.cost
        
        

def run(inputFilePath):
    with open(inputFilePath, 'r') as inputFile:
        with open(inputFilePath+'.txt', 'w') as outputFile:
            T = int(inputFile.readline())
            print("The input file contains", T, "test cases")
            for t in range (1, T+1):
                print("Processing case #" + str(t))
                input = inputFile.readline().split()
                A = int(input[0])
                N = int(input[1])
                print("A=", A, "N=", N)
                motes = [int(x) for x in inputFile.readline().split()]
                output = ''.join(["Case #", str(t), ": ",
                                 str(Game(A, sorted(motes)).solve()), "\n"])
                print(output)
                outputFile.write(output)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print ("Usage: ", sys.argv[0], "input-file")
        exit(0)
    inputFilePath = sys.argv[1]
    print("Working on input file: [", inputFilePath, "].")
    if not os.path.isfile(inputFilePath):
        print ("Error: the input file is not a valid file")
        exit(1)
    run(inputFilePath)
    print('End.')
    
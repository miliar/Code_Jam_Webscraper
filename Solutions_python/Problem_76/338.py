import random

class ProblemC():
    def __init__(self):
        self.fileInput = open("C-large.in", 'r')
        self.fileToPrint = open("out3Large.data", "a")

    def printToFile(self, n, result):
        self.fileToPrint.write("Case #" + n + ": " + str(result) + "\n")

    def algorythm(self):
        case = 1
        T = int(self.fileInput.readline())
        
        while (T > 0):

            result = 0
            
            N = self.fileInput.readline()

            C = self.fileInput.readline().split(" ")

            min = int(C[0])
            sum = 0
            
            for candy in C:
                result ^= int(candy)
                
                if(min>int(candy)):
                    min = int(candy)
                    
                sum += int(candy)
            
#            print result

            if(result != 0 ):
                result = "NO"
            else:
                result = sum - min
                
            self.printToFile(str(case), result)
            T -= 1
            case += 1

ddff = ProblemC()
ddff.algorythm()
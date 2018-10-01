import random

class ProblemA(file):
    def __init__(self):
        self.fileInput = open("A-large.in", 'r')
        self.fileToPrint = open("Output.data", "a")
        self.Orange = [1,0]
        self.Blue = [1,0]
        self.time = 0

    def printToFile(self, n, time):
        self.fileToPrint.write("Case #" + n + ": " + time + "\n")
        
    def algorythm(self):
        case = 1
        T = int(self.fileInput.readline())
        print "T = " + str(T)
        while (T > 0):
            line = self.fileInput.readline()
            massLine = line.split(" ")
            steps = int(massLine[0])
            
#            print "Steps = " + str(steps)
            
            self.time = 0
            i = 1
            unlimO = 0
            unlimB = 0
            
            self.Orange.insert(0, 1)
            self.Blue.insert(0, 1)
            
            while (steps * 2 > i):
                
                robot = massLine[i]
                buttom = massLine[i+1]

#                print "Robot = " + str(robot) + " | Buttom = " + str(buttom)
                
                if(robot == "O"):
                    step = abs(int(self.Orange[0]) - int(buttom)) + 1
                    if((step - unlimB) <= 0):
                        self.time += 1
                        unlimO += 1
                    else:
                        unlimO += (step - unlimB)
                        self.time += (step - unlimB)
                    
                    unlimB = 0
                    self.Orange.insert(0, buttom)
                    
                if(robot == "B"):
                    step = abs(int(self.Blue[0]) - int(buttom)) + 1
                    
                    if((step - unlimO) <= 0):
                        self.time += 1
                        unlimB += 1
                    else:
                        
                        unlimB += (step - unlimO)
                        self.time += (step - unlimO)
                    
                    unlimO = 0
                    self.Blue.insert(0, buttom)
                    
                i += 2
            self.printToFile(str(case), str(self.time))
            T -= 1
            case += 1

test = ProblemA()
test.algorythm()
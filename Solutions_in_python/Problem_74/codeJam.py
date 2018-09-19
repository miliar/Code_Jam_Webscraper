# Basically each robot is always working to get to his next goal on the sequence

def testCaseRunner(sequence):
    seconds=0
    r1=Robot("O",sequence)
    r2=Robot("B",sequence)
    while True:
        seconds=seconds+1
        #print seconds
        output1=r1.nextAction(sequence)
        output2=r2.nextAction(sequence)
        if(output1 or output2):
            sequence=sequenceMaker(sequence.split()[2:]).lstrip()
            #print sequence
        if(not sequence):
            break
    return seconds

def sequenceMaker(myList):
    result=""
    for item in myList:
        result=result+" "+item
    return result

class Robot():
    def __init__(self,string,sequence):
        self.name=string
        self.sequenceLeft=sequence
        self.pos=1
        self.goalPos=self.determineNewGoal()

    def nextAction(self,sequenceLeft):
        #print "Goal: "+str(self.goalPos)+" Position: "+str(self.pos)
        self.sequenceLeft=sequenceLeft # Updating local sequence state
        if(self.goalPos==self.pos and self.whoseTurn()==self.name):
            self.sequenceLeft=sequenceMaker(self.sequenceLeft.split()[2:]).lstrip()
            self.goalPos=self.determineNewGoal()
            #print self.name + " pressed the button!"
            return True # Presses button
        else:
            if (self.goalPos>self.pos):
                self.pos=self.pos+1
                #print self.name +" moves to "+str(self.pos)
            elif(self.goalPos<self.pos):
                self.pos=self.pos-1
                #print self.name +" moves to "+str(self.pos)
            
            return

    def determineNewGoal(self):
        flag=False
        for term in self.sequenceLeft.split():
            if(term==self.name):
                flag=True
            elif(flag==True):
                return int(term)
        return self.pos

    def whoseTurn(self):
        return self.sequenceLeft.split()[0]

def runner(fileName):
    fileHandle=open(fileName)
    noOfCases=fileHandle.readline()
    for n in range(1,int(noOfCases)+1):
        sequence=fileHandle.readline()
        sequence=sequenceMaker(sequence.split()[1:]).lstrip()
        print "Case #"+str(n)+": "+str(testCaseRunner(sequence))

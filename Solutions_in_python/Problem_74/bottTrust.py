from scanner import Scanner
import sys
def main():

    f= open("answer.txt", "w")
    #print(sys.argv[1])
    s  = Scanner(sys.argv[1])
    x = s.read_token() 
    #x = eval(input(""))
    for i in range(int(x) ):
        string = ""
        counts = s.read_token()
        string += counts
        for j in range(int(counts)):
            j = s.read_token()
            string += " " + j
            j= s.read_token()
            string += " " + j  
        #print(string)        
        #x = eval(input(""))
        #botString = input("")
        c = findSeq(string)
        #print("Case #", ( i+1), ": ",(c.getCount()))i
        number = str(i+1)
        print("Case #" + number + ": " + c.getCount())
        newstring = "Case #" + number + ": " + c.getCount()
        f.write(newstring + "\n")



class findSeq:


    def __init__(self, str):
        self.buttonsToPush = 0
        self.oragneLoc = 1
        self.blueLoc = 1
        self.blueList = []
        self.orangeList = []
        self.orangeLoc = 1
        self.pushOrangeNext = True
        self.seconds = 0
        self.seq =[]
        self.makeList(str)
        self.makeCount()

    def getCount(self):
        return str(self.seconds)

    def makeCount(self):
        go = True
        while(go):
            if self.seq[0] == "O":
                self.pushOrangeNext = True
            else:
                self.pushOrangeNext = False
            if len(self.blueList) != 0:
                if self.blueLoc < (self.blueList[0]):
                    self.blueLoc += 1
                elif self.blueLoc > self.blueList[0]:
                    self.blueLoc -= 1
                elif self.blueLoc == self.blueList[0] and self.pushOrangeNext == False:
                    self.blueList.pop(0)
                    self.seq.pop(0)
                    self.seq.pop(0)
            if len(self.orangeList) != 0:
                if self.orangeLoc < self.orangeList[0]:
                    self.orangeLoc += 1
                elif self.orangeLoc > self.orangeList[0]:
                    self.orangeLoc -= 1
                elif self.orangeLoc == self.orangeList[0] and self.pushOrangeNext == True:
                    self.orangeList.pop(0)
                    self.seq.pop(0)
                    self.seq.pop(0)
            self.seconds += 1
            #print(self.seconds) 
            if len(self.seq) == 0:
                go = False


    def makeList(self, str):
        Seq = str.split(" ")
        self.buttonsToPush = int(Seq[0])
        seqLen = len(Seq)
        self.seq = Seq[1:seqLen]
        for i in range(0, len(self.seq), 2 ):
            if self.seq[i] == "O":
                self.orangeList.append( int(self.seq[i+1]) )
            else:
                self.blueList.append( int(self.seq[i +1]))
        #print(self.blueList)
        #print(self.orangeList)
                
                
        


main()

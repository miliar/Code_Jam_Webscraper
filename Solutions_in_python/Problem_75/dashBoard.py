from scanner import Scanner
import sys

def main():

    f= open("answer.txt", "w")
    s = Scanner(sys.argv[1])
    x = s.read_token()
    x = int(x)
    for i in range(x):
        c = s.read_token()
        combineList = []
        c = int(c)
        for j in range(c):
            n = s.read_token()
            combineList.append(n)
        d = s.read_token()
        opposedList = []
        d = int(d)
        for k in range(d):
            n = s.read_token()
            opposedList.append(n)
        N= s.read_token()
        charList = []
        N = int(N)
        for L in range(N):
            n = s.read_char()
            charList.append(n)
        dash = Dashrules(combineList, opposedList, charList)
        f.write("Case #" + str(i+1)+": " +"[")
        if( len(dash.getFinal()) >0 ):
            for m in range(len(dash.getFinal()) -1):
                f.write(dash.getFinal()[m] + ", ")
            f.write(dash.getFinal()[-1])
        f.write("]\n")

class Dashrules:

    def __init__(self, coms , opps , chars):
        self.combineList = []
        self.combineDic = {}
        self.opposedList = []
        self.charsList = chars
        self.completeList(coms, opps)
        self.finalList = []
        self.doRules()
        #print(self.finalList)

    def getFinal(self):
        return (self.finalList)
    
    def doRules(self):
        for i in range( len(self.charsList) ):
            self.finalList +=  self.charsList[i]
            #create combine list if possible`
            if( len(self.finalList) >1 ):
                firstC = self.finalList[-2]
                secondC = self.finalList[-1]
           
            if( len(self.finalList) >1 and( ( [ firstC ,secondC ] in self.combineList) or ( [secondC , firstC] in self.combineList))  ):
                 
                #print(self.finalList[-2] +self.finalList[-1] )
                
                replace = self.combineDic[self.finalList[-2] +self.finalList[-1] ]
                self.finalList.pop(-1)
                self.finalList.pop(-1)
                self.finalList.append(replace)
            elif( len(self.finalList) >1): 
                for j in range(len(self.opposedList)):
                 
                    if self.opposedList[j][0] in self.finalList and self.opposedList[j][1] in self.finalList:
                        self.finalList = []
                        
        

    def completeList(self, coms , opps):
        for i in range(len(coms)):
            firstChar = coms[i][0]
            secondChar = coms[i][1]
            thirdChar = coms[i][2]
            self.combineDic[firstChar + secondChar] = thirdChar
            self.combineDic[secondChar + firstChar] =  thirdChar
            self.combineList.append([firstChar, secondChar ])
        for i in range(len(opps)):
            firstChar = opps[i][0]
            secondChar = opps[i][1]
            self.opposedList.append([firstChar, secondChar ])
             

main()

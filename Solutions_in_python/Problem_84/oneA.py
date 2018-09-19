from scanner import *
import sys

def main():
    f= open("answer.txt", "w")

    s = Scanner(sys.argv[1])
    x = s.read_token()
    x = int(x)
    for i in range(x):
        t = s.read_token()
        t2 = s.read_token()
        t = int(t)
        t2= int(t2)
        #print(t2)
        #print(t)
        matrix = []
        MOM = []
        for k in range(t):
            for j in range(t2):
                token = s.read_char()
                matrix.append(token)
            MOM.append(matrix)
            matrix = []
        print(MOM)
        sort = sortOut(MOM)
        word =sort.ispossible()
        print(sort.ispossible())
        print("this print")
        number = str(i+1)
        if( word== "False"):
            newstring = "Case #" + number + ": " + "\nImpossible \n"
            f.write(newstring )
        else:
            newstring = "Case #" + number + ": " + "\n"
            f.write(newstring)
            for j in range(len(sort.getMOM()) ):
                for k in range (len(sort.getMOM()[j] )):
                    string = (sort.getMOM()[j][k])
                    #print(string)
                    f.write(string)
                f.write("\n")
        
class sortOut:
    def __init__(self, MOM):
        self.MOM = MOM
        self.possible = "True"
        self.checkAndChange()
        print(self.MOM)

    def ispossible(self):
        return self.possible
    def getMOM(self):
        return self.MOM
    

    def checkAndChange(self):
        for i in range(len(self.MOM)):
            for j in range(len(self.MOM[i])):
                if( self.MOM[i][j] == "#"):
                    if( len(self.MOM[i]) <= j + 1 or self.MOM[i][j+1] == "."):
                        self.possible = "False"
                    elif(len(self.MOM) <= i + 1 or self.MOM[i+1][j]== "."):
                        self.possible = "False"
                    elif( self.MOM[i+1][j+1]== "." ):
                        self.possible = "False"
                    else:
                        self.MOM[i][j] = "/"
                        self.MOM[i][j+1] = "\\"
                        self.MOM[i+1][j] = "\\"
                        self.MOM[i+1][j+1] = "/"

                    

                        
main()

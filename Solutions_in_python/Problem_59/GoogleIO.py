'''
Created on 06/05/2010

@author: Administrator
'''
import sys
class googleIO(object):
    '''
    classdocs
    '''
    
    numOfCases=0
    inputFile = ()
    outputFile =()
    def __init__(self):
        '''
        Constructor
        '''
        self.inputFile=open('c:\\google\\A-large.in', 'rU')
        self.outputFile=open('c:\\google\\A-large.out', 'w')
  
        
    def getInput(self):
        existingDirs=[]
        newDirs=[]
        cases={}
        
      
        numOfCases=int(self.inputFile.readline())
        for n in range(0, numOfCases):
            line=self.inputFile.readline()
            (numOfExistingDirs,numOfnewDirs)=line.split()
            for dir in range (0,int(numOfExistingDirs)):
                existingDirs.append(self.inputFile.readline().rstrip())
            for dir in range (0,int(numOfnewDirs)):
                newDirs.append(self.inputFile.readline().rstrip())
            cases[n]=(existingDirs,newDirs)
            existingDirs=[]
            newDirs=[]
        
        return (numOfCases,cases)
          
     
     
    def writeOutput(self,data):
        if type(data).__name__=='list':
            for line in data:
                if line.endswith("\n"):
                    self.outputFile.write(line)
                else:
                    self.outputFile.write(line+"\n")    
        elif type(data).__name__=='str':
            if data.endswith("\n"):
                    self.outputFile.write(data)
            else:
                    self.outputFile.write(data+"\n")    
        else:
            print "wrong output type", type(data).__name__
    
        
        
    def getNumOfCases(self):
        return self.numOfCases

if __name__ == "__main__":
   
    IO = googleIO()
    #get the data from file
    IO.getInput()
   
        
    
   
  
    
        
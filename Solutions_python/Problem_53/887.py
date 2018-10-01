'''
Created on 08/05/2010

@author: Administrator
'''
import GoogleIO
import snapper
import sys
import operator

if __name__ == '__main__':
   
    cases = {}
    binary=[]
    IO = GoogleIO.googleIO()
    #get the data from file
    (numOfCases,cases)=IO.getInput()
    
    for n in range(0, numOfCases):
        (numOfSnappers,numOfSwitches)=cases[n]
        
    #    snaper = snapper.SnapperClass(int(numOfSnappers))
    #    snaper.switcher(int(numOfSwitches))
        binary ='1'*int(numOfSnappers)
        if operator.mod(int(numOfSwitches)+1,int(binary,2)+1)==0:
            output ="Case #%d: %s" % (n+1,"ON")
        else:
             output ="Case #%d: %s" % (n+1,"OFF")
 #       if snaper.checkLight()==True :
    #        output ="Case #%d: %s" % (n+1,"ON")
     #   else:
    #        output ="Case #%d: %s" % (n+1,"OFF")
            
        IO.writeOutput(output)
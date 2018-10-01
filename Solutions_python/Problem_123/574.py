'''
Created on 04/05/2013

@author: Carles
'''

def trataCaso(inFile):
    
    seNecesita = False
    numOperaciones = 0
    numAnadidosTotal = 0
    
    linea = inFile.readline()
    mySize = int(linea.partition(' ')[0])
    nMotes = int(linea.partition(' ')[2])
    
    motes = [None]*nMotes
    linea = inFile.readline()
    
    for i in range(nMotes):
        motes[i] = int(linea.partition(' ')[0])
        linea = linea.partition(' ')[2]
        if mySize <= motes[i]:
            seNecesita = True
    
    if not seNecesita:
        return numOperaciones
    else:
        motes.sort()
        for i in range(nMotes):
            if mySize > motes[i]:
                mySize += motes[i]
            else:
                numAnadidos = 0
                while(numAnadidos < nMotes - i):
                    mySize += mySize -1
                    numAnadidos += 1
                    if(mySize > motes[i]):
                        numOperaciones += numAnadidos
                        mySize += motes[i]
                        break
                        
                else:
                    numOperaciones += nMotes - i
                    break;
                
        return numOperaciones
        
    
    
def main():
    inFile = open('input.in', 'r')
    outFile = open('output.out', 'w')


    numCasos = int(inFile.readline())
    

    for i in range(numCasos):
        outFile.write("Case #"+str(i+1)+": "+str(trataCaso(inFile))+"\n")
        #print trataCaso(inFile)
        
if __name__ == "__main__":main()
#!/usr/bin/python2.6 -tt
import sys
sys.setrecursionlimit(1000000)
def openFile(path, right):
    file = open(path, right)
    return file
    
def closeFile(file):
    file.close()    
    
def warGame(b, n, k):
    points = 0
    
    def naomichoice():
        c = n[0]
        n.remove(n[0])
        return c
        
    def fight(nao):
        for i in range(len(k)):
            if k[i] > nao:
                # print("k: "+ str(k[i]) +" > "+ str(nao))
                k.remove(k[i])
                return 0
        # print("Nao: "+str(nao) +" > "+ str(k[0]))    
        k.remove(k[0])
        return 1
    
    for i in range(b):
        points += fight(naomichoice())
        
    return points
    
def deceitfulWarGame(b, n, k):
    points = 0
    print(str(n))
    print(str(k))
    
    def fight(nao):
        for i in range(len(k)):
            if k[i] > nao:
                #print("k: "+ str(k[i]) +" > "+ str(nao))
                k.remove(k[i])
                return 0
        #print("Nao: "+str(nao) +" > "+ str(k[0]))
        k.remove(k[0])
        return 1
                
    def naomichoice():
        if len(n) == 1:
            choice = n[0]
            n.remove(n[0])
            return choice

        for i in range(len(n)):
            canBeatMe = False
            for j in range(len(k)):
                if n[i] > k[j]:
                    canBeatMe = True
            if canBeatMe == False:
                #print(str(n[i]))
                n.remove(n[i])
                return k[len(k)-1] - 0.00000001    
                    
        choice = n[len(n) - 1]             
        n.remove(n[0]) 
        return choice           
    
    for i in range(b):
        points += fight(naomichoice())    
    
    return points

def main():
    path = "source.in"
    output = "output"
    file = openFile(path, "rU")
    outputFile = openFile(output, "wb")
    
    for i in range(int(next(file))):
        outputFile.write(str("Case #" + str( i + 1 ) + ": "))         
        blocks = int(next(file))
        naomis = sorted(map(float, next(file).split()))
        kens   = sorted(map(float, next(file).split()))
        naomis2 = naomis[:]
        kens2 = kens[:]
        outputFile.write(str(deceitfulWarGame(blocks, naomis, kens)))
        outputFile.write(" ")
        outputFile.write(str(warGame(blocks, naomis2, kens2)))
        outputFile.write("\n")
        # print("--------------------------------------------")
        
    closeFile(file)
    closeFile(outputFile)
	
#launch the main function
if __name__ == '__main__':
	main()
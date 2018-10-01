#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      makkron
#
# Created:     08/04/2017
# Copyright:   (c) makkron 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys

def main():
    nbSample=int(input())

    for idSample in range(nbSample):
        sample=sys.stdin.readline().split()
        #print(sample)
        sizeFlips=int(sample[1])
        pancakes=list(sample[0])
        validPancakes=True
        ctFlips=0
        for idPancake in range(0,len(pancakes)+1-sizeFlips):
            if pancakes[idPancake] == "-":
                ctFlips+=1
                for idFlip in range(idPancake,idPancake+sizeFlips):
                    if pancakes[idFlip] == "-":
                        pancakes[idFlip] = "+"
                    else:
                        pancakes[idFlip] = "-"
                #print(pancakes)
        for idPancake in range(len(pancakes)+1-sizeFlips,len(pancakes)):
            if pancakes[idPancake] == "-":
                validPancakes=False
        if validPancakes:
            print("Case #{}: {}".format(idSample+1,ctFlips))
        else:
            print("Case #{}: IMPOSSIBLE".format(idSample+1))

if __name__ == '__main__':
    main()

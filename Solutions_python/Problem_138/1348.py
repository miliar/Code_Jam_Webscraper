#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      qmarchal
#
# Created:     11/04/2013
# Copyright:   (c) qmarchal 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os,math,sys,copy
f = open("input.txt")
T = int(f.readline())

def WriteOutput(output):
    w = open("ouput.txt","w")
    w.write(output)
    w.close()
def Print(string):
    sys.stdout.write(str(string)+"\n")
def NextInt():
    return int(f.readline())
def NextList():
    return f.readline().split()
def NextIntList():
    strings = f.readline().split()
    ints = []
    for string in strings:
        ints.append(int(string))
    return ints
def NextFloatList():
    strings = f.readline().split()
    floats = []
    for string in strings:
        floats.append(float(string))
    return floats
def NextStr():
    string = str(f.readline())
    return string.replace('\n',"")
def Main():
    output = ""
    for t in range(1,T+1,1):
        output +="Case #%d: "%t + Case() + "\n"
    WriteOutput(output)
def Case():
    N = NextInt()
    TN = NextFloatList()
    TN.sort()
    TK = NextFloatList()
    TK.sort()
    deck = TK.copy()
    dw = N
    w = N
    output = ""
    for chosenN in TN:
        for wood in deck:
            if wood>chosenN:
                deck.remove(wood)
                w-=1
                break
    deck = TK.copy()
    for chosenN in TN:
        if chosenN<deck[0]:
            deck.remove(deck[len(deck)-1])
            dw-=1
        else:
            deck.remove(deck[0])
    return str(dw) + " " + str(w)
if __name__ == '__main__':
    Main()

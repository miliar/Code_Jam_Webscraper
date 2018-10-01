# @author: Raviphol Sukhajoti
# LANG : PY
# TASK : C
from __future__ import print_function
import sys,math,triangle

def IO():
    global fin
    infile = raw_input("Input File : ")
    outfile = raw_input("Output File : ")
    if len(infile) > 3 and infile[-3:] == '.in': 
        infile = infile[:-3]
    if not outfile == '' :
        if len(outfile) > 4 and outfile[-4:] == '.out': outfile = outfile[:-4]
        sys.stdout = open(outfile+'.out','w')
    fin = open(infile+'.in','r') 

def complete():
    sys.stdout = sys.__stdout__
    fin.close()
    print("completed.")
    
def adjust():
    for y in range(1,101):
        for x in range(1,101):
            if (table[y][x-1] == 1) and (table[y-1][x] == 1 and table[y][x] == 0):
                table[y][x] = 2
    for y in range(100,0,-1):
        for x in range(100,0,-1):
            if not(table[y][x-1] == 1 or table[y-1][x] == 1):
                table[y][x] = 0
    for i in range(1,101):
        table[0][i] = 0
        table[i][0] = 0
    for y in range(1,101):
        for x in range(1,101):
            if table[y][x] == 2: table[y][x] = 1

def dieall():
    for y in range(0,101):
        for x in range(0,101):
            if table[y][x] == 1: return False
    return True

def printTable():
    for y in range(0,7):
        for x in range(0,7):
            print(table[y][x],end='')
        print()

if __name__ == '__main__':
    IO()
    T = int(fin.readline())
    for t in range(1,T+1):
        ans = 0
        R = int(fin.readline())
        table = [[0 for i in range(101)]for j in range(101)]
        for i in range(R):
            x1,y1,x2,y2 = [int(x) for x in fin.readline().split(' ')]
            for y in range(y1,y2+1): 
                for x in range(x1,x2+1): table[y][x] = 1
        while not dieall(): 
            adjust()
            ans += 1            
        print('Case #%d:'%t,ans)
    complete()
    
    
import csv, sys, random, math

def flip(substr):
    numLetters = len(substr)
    newStr = ""
    for i in range(numLetters):
        if substr[i] == '+':
            newStr += '-'
        else:
            newStr += '+'
    return newStr            
    
def solve(pancakeStr, K):
    numPancakes = len(pancakeStr)
    newStr = ""
    numFlips = 0
    for i in range(numPancakes - K + 1):
        if pancakeStr[i] != '+':
            numFlips += 1
            pancakeStr = pancakeStr[0:i] + flip(pancakeStr[i:i+K]) + pancakeStr[i+K:]
            #print("Pancake String is: " + pancakeStr)
    return pancakeStr, numFlips

target = open("prob1_large_out.txt", 'w')
with open('prob1_large.txt','r') as f:
    T = int(f.readline())
    for i in range(T):
        stuff = f.readline().split()
        K = int(stuff[1])
        case_num = str(i+1)
        finalStr, numFlips = solve(stuff[0], K)
        if finalStr.find('-') == -1 :
            sol_str = 'Case #' + case_num +  ': ' + str(numFlips) + '\n'
        else:
            sol_str = 'Case #' + case_num +  ': ' + "IMPOSSIBLE" + '\n'
        target.write( str(sol_str) )
        
    







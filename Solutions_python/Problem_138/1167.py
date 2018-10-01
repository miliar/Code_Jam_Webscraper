#!/usr/bin/python
import sys

def scoreWar(allb):
    score = 0
    l = len(allb) / 2
    
    for k in range(l):
        chosenNaomi = minScoreNoami(allb)
        chosenKen = minScoreKen(allb, chosenNaomi[0])
        if chosenNaomi[0] > chosenKen[0]:    
            score += 1
    return score
 
def minScoreNoami(allb):
    a = -1
    
    for i in range(len(allb)):
        if allb[i][1] == 1:
            a = i
            break
    
    return allb.pop(a)
    
def minScoreK(allb):
    a = -1
    
    for i in range(len(allb)):
        if allb[i][1] == 2:
            a = i
            break
    
    return allb.pop(a)
    
def maxScoreKen(allb):
    a = -1
    
    for i in range(len(allb) - 1, -1, -1):
        if allb[i][1] == 2:
            a = i
            break
    
    return allb.pop(a)
    
def maxScoreNoami(allb):
    a = -1
    
    for i in range(len(allb) - 1, -1, -1):
        if allb[i][1] == 1:
            a = i
            break
    
    return allb.pop(a)
    
def minScoreKen(allb, naomiScore):
    a = -1
    minKindex = 0
    hasMinK = False
    
    for i in range(len(allb)):
        if not hasMinK and allb[i][1] == 2:
            minKindex = i
            hasMinK = True
        if allb[i][1] == 2 and allb[i][0] > naomiScore:
            a = i
            break
    
    if a == -1:
        return allb.pop(minKindex)  
    
    return allb.pop(a)

def scoreCheat(allb):
    score = 0
    
    for k in range(len(allb) / 2):
        if allb[-1][1] == 2: # OK
            chosenNaomi = minScoreNoami(allb)
            allb.pop()
        elif allb[0][1] == 1: # OK
            allb.pop(0)
            chosenKen = maxScoreKen(allb)
        else:
            chosenNaomi = minScoreNoami(allb)
            chosenKen = minScoreK(allb)
            if chosenNaomi[0] > chosenKen[0]:    
                score += 1
    return score


if (len(sys.argv) != 2):
  print "Usage: python " + sys.argv[0] + " inputFilename"
  exit()

inputf = open(sys.argv[1], 'r')
outputf = open('output.txt', 'w')

T = int(inputf.readline())

for t in range(T):
    N = int(inputf.readline())
    
    line = inputf.readline()
    s1 = line.split(' ')
    line = inputf.readline()
    s2 = line.split(' ')
    
    b1 = []
    b2 = []
    
    for i in range(N):
        b1.append([float(s1[i]), 1])
        b2.append([float(s2[i]), 2])
    
    allb = b1 + b2
    allb.sort()
    
    outputf.write('Case #')
    outputf.write(str(t+1))
    outputf.write(': ')
    allb_bak = allb[:]
    outputf.write(str(scoreCheat(allb)))
    outputf.write(' ')
    outputf.write(str(scoreWar(allb_bak))) # ANSWER
    outputf.write('\n')
    

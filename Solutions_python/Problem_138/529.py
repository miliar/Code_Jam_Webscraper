'''
Created on Apr 11, 2014

@author: mandy
'''
import sys

numLinesPerTest = 3

def deceitfulWar(fileName):
    f = open(fileName, 'r')
    lines = f.readlines()
    numTests = int(lines[0])
    
    for i in xrange(numTests):
        numBlocks = int(lines[i*numLinesPerTest+1].strip('\n'))
        naomi = map(float, lines[i*numLinesPerTest+2].strip('\n').split(' '))
        ken = map(float, lines[i*numLinesPerTest+3].strip('\n').split(' '))
        print 'Case #'+str(i+1)+': '+str(playDWar(list(naomi), list(ken), numBlocks))+' '+str(playWar(naomi, ken, numBlocks))

def playWar(naomi, ken, numBlocks):
    score = 0
    for n in naomi:
        mindiff = 10e7
        minItem = None
        for k in ken:
            diff = k-n
            if mindiff > diff and diff >0:
                mindiff = diff
                minItem = k
        if minItem:
            ken.remove(minItem)
            score+=1
    return numBlocks-score

def playDWar(naomi, ken, numBlocks):
    naomi.sort()
    ken.sort()
    while len(naomi)>0:
        allGreater = True
        for i in xrange(len(naomi)):
            if naomi[i] < ken[i]:
                naomi.remove(naomi[0])
                ken.remove(ken[len(ken)-1])
                allGreater = False
                break
        if allGreater:
            break
    return len(naomi)

def main():
    currentPath = sys.argv[0]
    currentPath = currentPath[:currentPath.rfind('/')]
    file = currentPath+'/D-large.in'
    deceitfulWar(file)

if __name__ == '__main__':
    main()
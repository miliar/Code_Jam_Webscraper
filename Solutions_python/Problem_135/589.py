#!python2
'''
Created on Apr 11, 2014

@author: Mike
'''

import sys


def findCard(line1, line2):
    ansList = []
    
    for c in line1:
        if c in line2:
            ansList.append(c)
    
    result = ""
    
    if ( len(ansList) == 1 ):
        result = ansList[0] 
    elif ( len(ansList) == 0 ):
        result = "Volunteer cheated!"
    elif ( len(ansList) > 1 ):
        result = "Bad magician!"
    
    return result

def openForWriting():
    from os.path import expanduser
    home = expanduser("~")
    path = home + '/git/GoogleCodeJam2014/Qualification/' + "mt.txt"
    
    wf = open(path, 'w')
    
    return wf

def readFile(fileName):
    from os.path import expanduser
    home = expanduser("~")
    path = home + '/Downloads/' + fileName 
    #print path
    f = open(path , 'r')
    
    wf = openForWriting()
    
    cases = int( f.readline() )
    
    i = 1
    while i <= cases:
        ans1 = int( f.readline() )
        l1 = []
        j = 0
        while j < 4:
            if (j == ans1 - 1):
                l1 = f.readline().rstrip("\n").split(" ")    
            else:
                f.readline()
            j += 1
        
        
        ans2 = int( f.readline() )
        l2 = []
        j = 0
        while j < 4:
            if (j == ans2 - 1):
                l2 = f.readline().rstrip("\n").split(" ")    
            else:
                f.readline()
            j += 1
        
        wf.write( ("Case #" + str(i) + ": " + findCard(l1, l2) + "\n").encode('UTF-8') )

        i += 1
        
        




if __name__ == '__main__':
    fileName = sys.argv[-1]
    readFile(fileName)
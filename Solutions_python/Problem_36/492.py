import sys
import string
import operator
import math
import re

# globals
infile = ''
N = 0
output = []
debug = False
p = 'welcome to code jam'


def processCase(i):
    global infile, currentLine, debug, p
    if debug:
        print '### processing case '+str(i+1)
    
    # read data
    s = infile[currentLine]
    currentLine += 1
    
    # solve the problem
    nMatch = findMatchTimes(s,p)
    
    string = (str(nMatch))[-4:]
    string = '0'*(4-len(string))+string
    return string


# find match times of subsequence
def findMatchTimes(s, p):
    if len(s)==0 and len(p)==0:
        return 1
    elif len(s)==0 and len(p)>0:
        return 0
    elif len(s)>0 and len(p)==0:
        return 1
    
    
    start = s.find(p[0])
    if start == -1:
        return 0
    
    i=start+1
    while i<len(s) and s[i]==p[0]:
        i+=1
    end = i-1
    nFirst = end-start+1
    
    nMatchTimes = nFirst*findMatchTimes(s[end+1:],p[1:]) + findMatchTimes(s[end+1:],p)
    return nMatchTimes
    
    
# Main procedure
infileName = sys.argv[1]
infile = open(infileName, 'r').readlines()
N=int(infile[0])
currentLine = 1

output = []
for i in range(N):
    result = processCase(i)
    output.append(result)
    
for i,v in enumerate(output):
    print 'Case #'+str(i+1)+':',v
    
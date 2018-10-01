
from collections import *
from copy import *
from math import *

if __name__=='__main__':
    input=open('A-large.in.txt','r+')
    output=open('A-large.out.txt','w+')
    numCases = int(input.readline().strip())
    for case in range(1,numCases+1):
        line = input.readline().strip().split()
        maxShy = int(line[0])
        shiness = []
        for i in range(maxShy+1):
            shiness.append(int(line[1][i]))

        numFriends = 0
        s = 0
        for i in range(maxShy+1):
            if s< i:
                numFriends+=i-s
                s=i
            s+=shiness[i]
        output.write("Case #%d: %d\n"%(case,numFriends))
        

    input.close()
    output.close()
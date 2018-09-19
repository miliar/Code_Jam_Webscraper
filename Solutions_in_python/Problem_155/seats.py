#! /usr/bin/python

import sys

def numFriends(line):
    tmp = line.split(" ")
    sMax = int(tmp[0])
    shynesses = map(int,tmp[1])
    standUp = 0
    friendsNeeded = 0
    for shyness,k in enumerate(shynesses):
        if standUp >= shyness:
            standUp += k
        else:
            friendsNeeded += (shyness - standUp)
            standUp += (k+(shyness - standUp))

    return friendsNeeded

def getData(fileName):
    f = open(fileName,'r+')
    lines = [line for line in f]
    lines = map(lambda x:x.replace("\n",""),lines)
    nCases = int(lines[0])
    k = 1
    while k <= nCases:
        tmpLine = lines[k]
        print "Case #"+str(k)+": "+str(numFriends(tmpLine))
        k = k+1


if __name__ == "__main__":
    fileName = sys.argv[1]
    getData(fileName)

#!/usr/bin/python

import sys

InputFile = "B-large.in"
OutFile = "B-large.out"

def processInput(filename):
    """docstring for processInput"""
    f = open(filename)
    data = [line.strip() for line in f.readlines()]
    #print data
    mapNum = int(data[0])
    #print mapNum
    index = 1
    length = 0
    inputMaps = []
    for i in range(mapNum):
        mapLen = int(data[index].split(' ')[0])
        tmpMap = []
        for tmpIndex in range(index + 1, index + 1 + mapLen):
            tmpMap.append([int(x) for x in data[tmpIndex].split(' ')])
        inputMaps.append(tmpMap)
        index += 1 + mapLen
    #print inputMaps
    return inputMaps

def processOutput(filename, content):
    """docstring for processOutput"""
    f = open(filename, 'w')
    for i in range(len(content)):
        f.write('Case #%d:\n' %(i + 1))
        for l in content[i]:
            f.write("%s\n" %(" ".join(chr(flag) for flag in l)))
    f.close()

def solve(maps):
    """docstring for solve"""
    ret = []
    print maps
    for m in maps:
        ret.append(drawMap(m))
    return ret

def drawMap(inputMap):
    """docstring for drawMap"""
    setList = []
    mapLen = len(inputMap)
    mapWidth = len(inputMap[0])
    retMap = []
    for index in range(mapLen):
        newlist = [None] * mapWidth
        retMap.append(newlist)
    for i in range(mapLen):
        for j in range(mapWidth):
            srcLati = inputMap[i][j]
            destLati = []
            destPos = []
            if i > 0:
                destLati.append(inputMap[i-1][j])
                destPos.append(str(i-1) + "#" + str(j))
            if j > 0:
                destLati.append(inputMap[i][j-1])
                destPos.append(str(i) + "#" + str(j-1))
            if j + 1 < mapWidth:
                destLati.append(inputMap[i][j+1])
                destPos.append(str(i) + "#" + str(j+1))
            if i + 1 < mapLen:
                destLati.append(inputMap[i+1][j])
                destPos.append(str(i+1) + "#" + str(j))
            if destLati:
                minLati = min(destLati)
            else:
                minLati = 10000
            if minLati < srcLati:
                src = str(i) + "#" + str(j)
                des = destPos[destLati.index(minLati)]
                exist = False
                for s in setList:
                    if src in s:
                        exist = True
                        if des not in s:
                            s.add(des)
                    if des in s:
                        exist = True
                        if src not in s:
                            s.add(src)
                if not exist:
                    newset = set()
                    newset.add(src)
                    newset.add(des)
                    setList.append(newset)
    #print setList
    for s in setList:
        for t in setList:
            if s & t:
                s |= t
    #print setList
    curChr = 97
    for i in range(mapLen):
        for j in range(mapWidth):
            if retMap[i][j] is None:
                retMap[i][j] = curChr
                curChr += 1
                s = str(i) + "#" + str(j)
                for index in range(len(setList)):
                    if s in setList[index]:
                        for element in setList[index]:
                            #print element
                            tmpstr = element.split('#')
                            m = int(tmpstr[0])
                            n = int(tmpstr[1])
                            retMap[m][n] = retMap[i][j]
                            #print retMap
                        index = len(setList)
    print retMap
    return retMap

def main():
    """docstring for main"""
    maps = processInput(InputFile)
    result = solve(maps)
    processOutput(OutFile, result)

if __name__ == '__main__':
    main()

#!/usr/bin/python
''' Usage %s
'''
import logging

CurrentDebugLevel=logging.DEBUG

class DirectionWrongException: pass

class Direction:
    DIR_NONE = 0
    DIR_NORTH = 1
    DIR_EAST = 2
    DIR_SOUTH = 3
    DIR_WEST = 4
    
# None, North, East, South, West
directionVector = [[-1, -1], [0, -1], [1, 0], [0, 1], [-1, 0]]

def checkFlow(latMap, width, height, x, y):
    direction = Direction.DIR_NONE
    minLat = latMap[y][x]
    if (y - 1 >= 0) and (minLat > latMap[y - 1][x]): # north
        minLat = latMap[y - 1][x] 
        direction = Direction.DIR_NORTH
    if (x - 1 >= 0) and (minLat > latMap[y][x - 1]):
        minLat = latMap[y][x - 1] 
        direction = Direction.DIR_WEST
    if (x + 1 < width) and (minLat > latMap[y][x + 1]):
        minLat = latMap[y][x + 1] 
        direction = Direction.DIR_EAST
    if (y + 1 < height) and (minLat > latMap[y + 1][x]):
        minLat = latMap[y + 1][x] 
        direction = Direction.DIR_SOUTH
    return direction

def MoveDirection(x, y, direction, width, height):
    if direction == Direction.DIR_NORTH and y - 1 >= 0: return [x, y - 1]
    if direction == Direction.DIR_EAST and x + 1 < width: return [x + 1, y]
    if direction == Direction.DIR_SOUTH and y + 1 < height: return [x, y + 1]
    if direction == Direction.DIR_WEST and x - 1 >= 0: return [x - 1, y]
    raise DirectionWrongException
        
def ScanMap(latMap, width, height):
    dirMap = []
    #resultMap.append(['a', 'b', 'c', "d", "e"])
    for y in range(0, len(latMap)):
        dirRow = []
        row = latMap[y]
        for x in range(0, len(row)):
            dirRow.append(checkFlow(latMap, width, height, x, y))
        dirMap.append(dirRow)
    
    return dirMap

def FlowWaterAndMark(dirMap, resultMap, curX, curY, curLabel):
    markCells = []
    while True: # while not a sink
        markCells.append([curX, curY])
        direction = dirMap[curY][curX]
        if direction == Direction.DIR_NONE: break
        curX += directionVector[direction][0]
        curY += directionVector[direction][1]
        
    mark = curLabel
    if resultMap[curY][curX] == '-':
        curLabel = chr(ord(curLabel) + 1) # advance to the next mark
    else: mark = resultMap[curY][curX] # use the same one
    
    for pos in markCells:
        resultMap[pos[1]][pos[0]] = mark
    return curLabel

def LabelBasin(dirMap, width, height):
    resultMap = [['-' for j in range(0, width)] for i in range(0, height)]
    curLabel = 'a'
    
    for y in range(0, height):
        for x in range(0, width):
            if resultMap[y][x] != '-': continue # already done
            curLabel = FlowWaterAndMark(dirMap, resultMap, x, y, curLabel)
            
    return resultMap

def ProcessCase(inFile, caseNum):
    logging.debug('Case %d', caseNum)
    param = inFile.readline().strip().split()
    height = int(param[0])
    width = int(param[1])

    latMap = []
    for i in range(0, height):
        latMap.append([int(x) for x in inFile.readline().strip().split()])
    
    for row in latMap: logging.debug(row)
    
    dirMap = ScanMap(latMap, width, height)
    
    logging.debug("Direction")
    for row in dirMap: logging.debug(row)
    
    resultMap = LabelBasin(dirMap, width, height)
    
    return resultMap

def OutputResult(outFile, caseNum, result):
    outFile.write("Case #{0}:\n".format(caseNum))
    logging.debug("Case #{0}:".format(caseNum))
    for i in result:
        printSpace = False
        for j in i:
            if printSpace: outFile.write(" ") 
            else: printSpace = True
            outFile.write(str(j))
        outFile.write("\n")
        logging.debug(i)

def ProcessDataFile(fileName):
    inFile = open(fileName, 'r')
    line = inFile.readline()
    lineCount = int(line)
    outFile = open(fileName + '.out.txt', 'w')
    for i in range(1, lineCount + 1):
        result = ProcessCase(inFile, i)
        OutputResult(outFile, i, result)
    outFile.close()

def main():
    logging.basicConfig(level=CurrentDebugLevel, datefmt='%Y.%m.%d %H:%M:%S', format='%(asctime)s %(levelname)-5s %(message)s')
    question = 'B'
    #dataSet = 'small-attempt0'
    dataSet = 'large'
    #dataSet = 'test'
    #dataSet = 'small-practice'
    #dataSet = 'large-practice'

    ProcessDataFile('{0}-{1}.in'.format(question, dataSet))

if __name__ == '__main__': main()
#!/bin/python


def getRobot (letter):
    # 0 for blue, 1 for orange
    if letter == "B": return 0
    else: return 1


def norm (x):
    return x / abs(x)


class Move (object):
    
    def __init__ (self, robot, button):
        self.robot = robot
        self.button = button
        self.nextMove = None
        self.nextOwnMove = None


class MoveList (object):
    
    def __init__ (self):
        self.firstMove = None
        self.lastMove  = None
        self.firstMoves = [None, None]
        self.lastMoves  = [None, None]
    
    def append (self, move):
        r = move.robot
        if not self.firstMove:      self.firstMove = move
        if not self.firstMoves[r]:  self.firstMoves[r] = move
        if not self.lastMove:       self.lastMove = move
        else:
            self.lastMove.nextMove = move
            self.lastMove = move
        if not self.lastMoves[r]:   self.lastMoves[r] = move
        else:
            self.lastMoves[r].nextOwnMove = move
            self.lastMoves[r] = move
    
    def __str__ (self):
        moveStrings = []
        move = self.firstMove
        while move:
            moveStrings.append("%d:%d" % (move.robot, move.button))
            move = move.nextMove
        return " ".join(moveStrings)


def readMoves (line):

    moves = MoveList()
    
    lineData = line.strip().split(" ")
    for i in range(len(lineData) / 2):
        
        robot = getRobot(lineData[2*i+1])
        button = int(lineData[2*i+2])
        move = Move(robot,button)
        moves.append(move)
    
    return moves


def stepRobot (pos, nextMoves, r):
    if not nextMoves[r]: return
    if nextMoves[r].button == pos[r]: return
    pos[r] += norm(nextMoves[r].button - pos[r])
    


def stepRobots (pos, nextMoves):
    for r in range(len(nextMoves)):
        stepRobot(pos, nextMoves, r)


def countSteps (moves):
    
    steps = 0
    pos = [1, 1]
    move = moves.firstMove
    nextMoves = moves.firstMoves[:]
    
    while move:
        while pos[move.robot] != move.button:
            steps += 1
            stepRobots(pos, nextMoves)
            #print "Moved to", pos
        steps += 1
        stepRobot(pos, nextMoves, (move.robot+1)%2)
        #print "Moved to", pos, "and", move.robot, "pressed button"
        
        nextMoves[move.robot] = move.nextOwnMove
        move = move.nextMove
    
    return steps


def main ():
    input = open("input.txt")
    testcases = int(input.readline())
    
    case = 0
    for line in input:
        case += 1
        moves = readMoves(line)
        steps = countSteps(moves)
        print "Case #%d: %d" % (case, steps)


if __name__ == "__main__": main()
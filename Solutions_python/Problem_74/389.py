#!/usr/bin/env python

import sys, re

#----------------------------------------------------------------------
colors = ['B','O']

def findNextTargetIndex(sequence, startFrom, color):

    if startFrom == None:
        return None

    while startFrom < len(sequence) and sequence[startFrom][0] != color:
        startFrom += 1

    if startFrom >= len(sequence):
        return None

    return startFrom

#----------------------------------------------------------------------

def solve(sequence):
    # print >> sys.stderr,sequence

    N = int(sequence.pop(0))

    # indices are 0 = blue, 1 = orange

    currentPos = [ 1, 1]
    targetPos = [ None, None ]

    # color (0 = blue, 1 = orange) which needs
    # to press a button next
    nextRobotActionColor = None

    # pull the next instruction from the list

    # next target to reach
    nextTargetIndex = 0

    # indices into sequence where the next target for each
    # color is found
    nextPerColorTargetIndex = [ findNextTargetIndex(sequence,0,0),
                                findNextTargetIndex(sequence,0,1),
                                ]

    fetchNewTarget = [ False, False ]

    pushingButton = [ False, False ]

    timeElapsed = 0
    while True:

        # check what we should do

        # print >> sys.stderr, timeElapsed,nextPerColorTargetIndex,"pos=",currentPos,'pushing=',pushingButton

        # for color in range(2):

        thisTimeButtonPushed = False
        for color in [1,0]:
            # check what we should do at each step
            if pushingButton[color]:
                # robot can move this round now
                pushingButton[color] = False
                # print >> sys.stderr, "setting pushing to false",timeElapsed,colors[color]

            if nextPerColorTargetIndex[color] == None:
                # already complete
                continue

                
            targetPos = sequence[nextPerColorTargetIndex[color]][1]

            # check whether we are at the target position 
            if targetPos != None:
                if targetPos > currentPos[color]:
                    # move this robot closer towards
                    # its target position
                    currentPos[color] += 1
                    # print >> sys.stderr, "robot",colors[color],"moves to",currentPos[color],"at time",timeElapsed
                elif targetPos < currentPos[color]:
                    currentPos[color] -= 1
                    # print >> sys.stderr, "robot",colors[color],"moves to",currentPos[color],"at time",timeElapsed
                else:
                    # we're already at the target position
                    # check whether it's our turn to push the button

                    # print >> sys.stderr, "FOO",nextPerColorTargetIndex,nextTargetIndex
                    if nextPerColorTargetIndex[color] == nextTargetIndex and not thisTimeButtonPushed:

                        # push the button
                        pushingButton[color] = True
                        thisTimeButtonPushed = True
                        
                        # print >> sys.stderr, "robot",colors[color],"pushes button",currentPos[color],"at time",timeElapsed
                        # note that the robot does not move now

                        nextPerColorTargetIndex[color] = findNextTargetIndex(sequence, nextPerColorTargetIndex[color] + 1, color) 
                        # print >> sys.stderr, "new target for ", timeElapsed,colors[color]
                        nextTargetIndex += 1
                    else:
                        # print >> sys.stderr, "robot",colors[color],"must wait at",currentPos[color],"at time",timeElapsed
                        pass

        # are we done ?
        if all([ x == None for x in nextPerColorTargetIndex ] ) and not any(pushingButton):
            return timeElapsed

        # if not any(pushingButton):
        #     # check whether we have met a new target
        #     testColor = sequence[nextTargetIndex][0]
        #     if sequence[nextTargetIndex][1] == currentPos[testColor]:
        #         # we reached the target, get next instruction
        #         nextTargetIndex += 1
        # 
        #         if nextTargetIndex >= len(sequence):
        #             # all targets met
        #             return timeElapsed


        timeElapsed += 1
            


#----------------------------------------------------------------------
# main
#----------------------------------------------------------------------
T = int(sys.stdin.readline())

for case in range(1,T+1):


    seq = re.split('\s+',sys.stdin.readline().split('\n')[0])

    N = int(seq[0])

    if len(seq) != 2*N+1:
        print >> sys.stderr,"length is wrong"


    newSeq = [ N ]
    seq.pop(0)

    for i,j in zip(seq[::2],seq[1::2]):

        j = int(j)

        if i == 'B':
            newSeq.append((0,j))
        elif i == 'O':
            newSeq.append((1,j))

    sol = solve(newSeq)

    print "Case #%d:" % case, sol

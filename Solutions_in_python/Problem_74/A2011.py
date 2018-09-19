##fin = open("input.in", "r")
##numCases = int(fin.readline())
##
##for i in range(numCases):
##    instructions = fin.readline().split()
##    numButtons = int(instructions[0])
##    time=0
##    orangePos=1
##    bluePos=1
##    pushedCounter=0 #counts which buttons have been pushed. should end at len(instructions)-2
##    counter=1 #counts where we are in the instructions, goes from 1 to numButtons*2, or len(instructions)-1
##    while pushedCounter != (numButtons*2-1):
##        time+=1 #increments time counter
##        pushedAlready = False 
##        colorNext=instructions[counter]
##
##        
##        if colorNext=="O":
##            counter+=1 #moves counter to the location of the button
##            if orangePos<int(instructions[counter]):
##                orangePos+=1
##                print pushedAlready
##            if orangePos>int(instructions[counter]):
##                orangePos-=1
##            if orangePos==int(instructions[counter]) and pushedAlready==False:
##                pushedAlready=True
##                print "Orange pushed" + str(time)
##                if pushedCounter==0:
##                    pushedCounter+=1
##                else:
##                    pushedCounter+=2 #increments pushedCounter to the next button
##                
##        if colorNext=="B":
##            counter+=1 #moves counter to the location of the button
##            if bluePos<int(instructions[counter]):
##                bluePos+=1
##            if bluePos>int(instructions[counter]):
##                bluePos-=1
##            if bluePos==int(instructions[counter]) and pushedAlready==False:
##                pushedAlready=True
##                print "blue pushed" + str(time)
##                if pushedCounter==0:
##                    pushedCounter+=1
##                else:    
##                    pushedCounter+=2 #increments pushedCounter to the next button
##
##    print "Time:" + time
#from Numeric import *


#returns where the next blue position is, given the instructions array
def scanNextBlue(array):
    for i in range(len(array)):
        if array[i]=="B":
            return array[i+1] #returns position
    return "none"
    
#returns where the next orange position is, given the instructions array
def scanNextOrange(array):
    for i in range(len(array)):
        if array[i]=="O":
            return array[i+1] #returns position
    return "none"


fin = open("A-small-attempt1.in", "r")
fout = open("output.txt", 'w')
numCases = int(fin.readline())

for i in range(numCases): #goes through each case
    instructions = fin.readline().split()
    numButtons = int(instructions[0])
    time=0
    orangePos=1
    bluePos=1
    
    colorOrder = []

    for j in range(numButtons):
        colorOrder.append(instructions[2*j+1]) #gets the order of the buttons for ex: [O,B,B,O]
        print "debug: " + str(colorOrder)

    buttonPushedCounter = -1 #increments up by 1 every time we finish pressing a button. points to the index of the button that has last been pushed. when it gets to numButtons-1 we're done

    while buttonPushedCounter<(numButtons-1): #when buttonPushedCounter = numButtons then we're done. remember to only update buttonPushedCounter after a button is pushed
        pushedAlready = False #two buttons can't be pushed in the same turn
        time+=1 #increments time
        if scanNextBlue(instructions)!="none":
            nextBluePos = int(scanNextBlue(instructions))
        elif scanNextBlue(instructions)=="none":
            nextBluePos = "none"
        if scanNextOrange(instructions)!="none":
            nextOrangePos = int(scanNextOrange(instructions))
        elif scanNextOrange(instructions)=="none":
            nextOrangePos = "none"
         
        if orangePos<nextOrangePos and nextOrangePos!="none":
            orangePos+=1
        elif (orangePos>nextOrangePos and nextOrangePos!="none"):
            orangePos-=1
        elif (orangePos==nextOrangePos and buttonPushedCounter<(numButtons-1) and colorOrder[buttonPushedCounter+1]=="O" and pushedAlready == False): #if it's at the right place and the button to be pressed is that one then press it
            buttonPushedCounter+=1 #pushes button
            pushedAlready = True
            instructions[buttonPushedCounter*2+1] = "D" #marks the button as done in instructions
            print "orange button pushed at location: " + str(orangePos) + "at time" + str(time)

        if bluePos<nextBluePos and nextBluePos!="none":
            bluePos+=1
        elif (bluePos>nextBluePos and nextBluePos!="none"):
            bluePos-=1
        elif (bluePos==nextBluePos and buttonPushedCounter<(numButtons-1) and colorOrder[buttonPushedCounter+1]=="B" and pushedAlready == False): #if it's at the right place and the button to be pressed is that one then press it
            buttonPushedCounter+=1 #pushes button
            pushedAlready == True
            instructions[buttonPushedCounter*2+1] = "D" #marks the button as done in instructions
            print "blue button pushed at location: " + str(bluePos) + "at time" + str(time)

        print "time: " + str(time) + " Blue pos: "+str(bluePos) + " Orange pos: "  + str(orangePos)

    fout.write("Case#" + str(i+1) + ": " + str(time) + '\n')
fout.close()




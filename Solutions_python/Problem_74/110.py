'''
Created on May 7, 2011

@author: doronv
'''

## import section
import re
import filecmp

## folder definitions
## input folder
rootFolder = 'C:/Documents and Settings/Doron Veltzer.DORON/My Documents/My Dropbox/Programming/GoogleCodeJam'
inputsFolder = 'inputs'
outputsFolder = 'outputs'
yearFolder = '2011'
stageFolder = 'Qual'
projectLetter = 'A'

example = False

if (example):
    fileName = projectLetter + '-def'
    examplePath = rootFolder + '/' + outputsFolder + '/' + yearFolder + stageFolder + '/' + fileName + '.example'
else:
    fileName = projectLetter + '-large'

inputPath = rootFolder + '/' + inputsFolder + '/' + yearFolder + stageFolder + '/' + fileName + '.in'
outputPath = rootFolder + '/' + outputsFolder + '/' + yearFolder + stageFolder + '/' + fileName + '.out'


## open input
input = open(inputPath, 'r')
output = open(outputPath, 'w')


## handle input
## read case number
match = re.search('(\d+)', input.readline())
T = int(match.group(1))

## iterate on all cases
for t in range(T):

    ## reset robot positions and time counter
    O = 1
    B = 1
    time = 0
    ## reset the robot free moves done while the other robot moves
    OSpares = 0
    BSpares = 0

    ## read line and split it to move number and moves
    line = input.readline()
    lineSplit = line.split(' ')
    N = int(lineSplit[0])

    ## parse moves and count the time
    for n in range(N):
        ## parse robot move instruction
        robot = lineSplit[2 * n + 1]
        button = int(lineSplit[2 * n + 2])
        
        ## move the right robot to the right place 
        if (robot == 'O'):
            ## time = distance + 1, distance is the distance to the pressed button - time spent by the other robot doing stuff 
            OTime = max(abs(button - O) - OSpares, 0) + 1
            time = time + OTime
            BSpares += OTime
            OSpares = 0
            O = button
        else:
            ## time = distance + 1, distance is the distance to the pressed button - time spent by the other robot doing stuff 
            BTime = max(abs(button - B) - BSpares, 0) + 1
            time = time + BTime
            OSpares += BTime
            BSpares = 0
            B = button

    ## output case result
    outputLine = 'Case #' + str(t + 1) + ': ' + str(time) + '\n'
    if (example):
        print(outputLine)
    output.write(outputLine)

input.close()
output.close()

## if this is an example run then compare the output to the example output file
if (example):
    if (filecmp.cmp(outputPath, examplePath)):
        print('Def result match OK')
    else:
        print('ERROR: Def result differ')

####print input.read()
##while 1:
####    char = input.read(1)          # read by character
##    line = input.readline()          # read by character
##    if not line: break
##    print line,


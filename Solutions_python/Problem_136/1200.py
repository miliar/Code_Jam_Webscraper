#!/usr/bin/python
import sys

def timeCookies(time, cookiesPerSec, costFarm, extraPerFarm, goal):
    while True:
        noFarm = goal / cookiesPerSec
        buildFarm = costFarm / cookiesPerSec
        cookiesPerSec += extraPerFarm
        waitAfterBuildFarm = goal / cookiesPerSec
        if (noFarm < buildFarm + waitAfterBuildFarm):
            time += noFarm
            break
        else:
            time += buildFarm
    return time

if (len(sys.argv) != 2):
  print "Usage: python " + sys.argv[0] + " inputFilename"
  exit()

inputf = open(sys.argv[1], 'r')
outputf = open('output.txt', 'w')

T = int(inputf.readline())

for t in range(T):

    line = inputf.readline()
    s = line.split(' ')
    
    costFarm = float(s[0])
    extraPerFarm = float(s[1])
    goal = float(s[2])
    cookiesPerSec = 2
    time = 0
    
    outputf.write('Case #')
    outputf.write(str(t+1))
    outputf.write(': ')
    outputf.write(str(timeCookies(time, cookiesPerSec, costFarm, extraPerFarm, goal)))
    outputf.write('\n')

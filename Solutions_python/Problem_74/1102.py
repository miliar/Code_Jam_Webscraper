'''
Created on Sep 3, 2009

@author: Robin
'''
import string

f=open('a.in', 'r')
mapCount = int(f.readline())
maps = []
for i in range(mapCount):
    line = string.split(f.readline())
    seq = line[1:]
    pos = [1, 1]
    finished = False
    index = 0
    time = 0
    extratime = [0,0]
    while not finished:
        robot = 0
        if seq[index] == "B":
            robot = 1
        newpos = int(seq[index+1])
        movingtime = abs(pos[robot] - newpos)
        t = movingtime - extratime[1 - robot]
        if t < 0:
            t = 0
        time += t + 1
        extratime[robot] += t + 1
        extratime[1 - robot] = 0
        pos[robot] = newpos
        index += 2
        if len(seq) <= index:
            finished = True
    
    
    print "Case #"+str(i+1)+": "+str(time)
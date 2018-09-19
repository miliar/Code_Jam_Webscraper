#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      wani
#
# Created:     08/05/2011
# Copyright:   (c) wani 2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import sys
import copy

def addtime(way,stam,run,walk,move,time):
    if stam == 0:
        time += way / (walk + move)
    elif way / (run + move) > stam:
        time += stam + ( way - stam*(run+move)) / (walk +move)
        stam = 0
    else:
        time += way / (run + move)
        stam -= way / (run + move)
    return time,stam

def gettime(dis,walk,run,stam,ways):
    ways2 = []
    normal = dis
    for way in ways:
        ways2.append([way[2],(way[1]-way[0])])
        normal = normal - (way[1] - way[0])
    ways2.append([0,normal])
    ways2.sort()
    time = 0
    for way2 in ways2:
        time,stam = addtime(way2[1],stam,float(run),float(walk),way2[0],time)
    return time

def main():
    f = open(sys.argv[1])
    fo = open(sys.argv[2],"w")

    cases = int(f.readline().strip())
    for i in range(cases):
        dis,walk,run,stam,num = [ int (x) for x in f.readline().strip().split()]
        ways = []
        for n in range(num):
            ways.append([int (x) for x in f.readline().strip().split()])
        g = gettime(dis,walk,run,stam,ways)
        out = "Case #%d: %s"%(i+1,g) + "\n"
        print out,
        fo.write(out)
    f.close()
    fo.close()

if __name__ == '__main__':
    main()

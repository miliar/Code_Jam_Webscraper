# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 08:47:28 2017

@author: kprashan
"""

T = int(input().rstrip())
speedForAnnie = 1.0000000000

for i in range(T):
    D,N = [int(num) for num in input().rstrip().split()]
    timeToFinish = []
    locDict = []
    
    for j in range(N):
        start, speed = [int(num) for num in input().rstrip().split()]
        locDict.append((start,speed))
        locDict.sort(key=lambda tup : tup[0])
#        print("locDict", locDict)

    for horse in locDict :
        finish = (D - horse[0])/horse[1]
        timeToFinish.append(finish)
#        print("Appending horse:", horse)
        maxTime = max(timeToFinish)
        speedForAnnie = D/maxTime
#    print("Horses:",locDict)
#    print(timeToFinish)
    print("Case #{}: {}".format(i+1, speedForAnnie))
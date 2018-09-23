# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 20:02:33 2017

@author: elon
"""

cases = int(raw_input())
for i in xrange(1, cases+1):
    pancakes, flips_per = raw_input().split(" ")
    flips_per = int(flips_per)
    finalpancakes = pancakes
    flips = 0
    for j in xrange(0, len(finalpancakes)-flips_per+1):
        if finalpancakes[j] == "-":
            flips+=1
            for l in xrange(0, flips_per):
                if finalpancakes[j+l] == "+":
                    finalpancakes = finalpancakes[:j+l] + "-" + finalpancakes[j+l+1:]
                elif finalpancakes[j+l] == "-":
                    finalpancakes = finalpancakes[:j+l] + "+" + finalpancakes[j+l+1:]
    notimpossible = True
    for j in xrange(len(finalpancakes)-flips_per, len(finalpancakes)):
        if finalpancakes[j] == "-":
            notimpossible = False
            break
    if notimpossible:
        print "Case #"+str(i)+": "+str(flips)
    else:
        print "Case #"+str(i)+": IMPOSSIBLE"
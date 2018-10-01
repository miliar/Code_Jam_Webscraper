#!/bin/python

f = open('B-large.in')

testcases = int(f.readline())
#print testcases

for i in range (testcases):
    production = 2
    farmCostTime = 0
    farmCost, farmProduction, goal = map(float, f.readline().strip().split(' '))
    farmTime = goal/production
    while True:
        farmTime = farmCost/production + goal / (production+farmProduction)
        if farmTime > goal/production:
            print "Case #%d: %.7f" % (i+1, farmCostTime + goal/production)
            break
        else:
            farmCostTime += (farmCost/production)
            production += farmProduction

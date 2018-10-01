#!/usr/local/bin/python3
import sys

# read input
with open(sys.argv[1]) as fd:
    lines = fd.read().split("\n")
    if lines[-1] == "": lines = lines[:-1]

lines.pop(0)
cases = [list(map(float, line.split(" "))) for line in lines]

for i, case in enumerate(cases):
    price, farmProduction, goal = case
    speed = 2.0
    elapsed = 0.0
    while True:
        timeToBuyFarm = price / speed
        timeToWin = goal / speed
        newTimeToWin = goal / (speed + farmProduction)
        if timeToBuyFarm + newTimeToWin < timeToWin:
            speed   += farmProduction
            elapsed += timeToBuyFarm
        else:
            elapsed += timeToWin
            break
    
    print("Case #{0}: {1:.7f}".format(i+1, elapsed))

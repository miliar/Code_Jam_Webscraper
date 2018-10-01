import sys
import collections
sys.setrecursionlimit(10000)

def solve(finName, function, step):
    fin = open(finName, "r")
    fout = open(finName+"out", "w")
    
    lines = fin.readlines()
    case = 1
    for i in range(1, int(lines[0]) * step + 1, step):
        args = [e.rstrip() for e in lines[i : i+step]]
        fout.write("Case #" + str(case) + ": " + function(args) + "\n")
        case += 1
        if case % 10000 == 0: print ("+10000")
    fin.close()
    fout.close()

def cookieClickerAlpha(args):
    baseCps = 2.0
    argsList = args[0].split(" ")
    farmCost = float(argsList[0])
    farmGain = float(argsList[1])
    win = float(argsList[2])

    currentCps = baseCps
    t = 0
    while True:
        tToWin = win / currentCps
        tToFarm = farmCost / currentCps
        tToWinFarm = (win) / (currentCps + farmGain)
        if tToWin <= tToFarm + tToWinFarm:
            t+=tToWin
            return str(t)
        else:
            t+=tToFarm
            currentCps += farmGain
    
if __name__=="__main__":
    solve("B-large.in", cookieClickerAlpha, 1)
    print("done")

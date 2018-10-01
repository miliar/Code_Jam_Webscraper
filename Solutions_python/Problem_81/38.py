#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      wani
#
# Created:     21/05/2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import sys

def getRPI(teams,scores):
    oppos,wps,games,wins = [],[],[],[]
    for score in scores:
        win = 0
        game = 0
        oppo = []
        for i,s in enumerate(score):
            if s == "0":
                game += 1
                oppo.append(i)
            elif s == "1":
                game += 1
                win += 1.0
                oppo.append(i)
        wps.append(win / game)
        wins.append(win)
        games.append(game)
        oppos.append(oppo)
#    print wps,oppos,wins
    owps = []
    for i in range(teams):
        ow = 0
        for j in oppos[i]:
            if scores[i][j] == "0":
                ow += (wins[j]-1.0) / (games[j] - 1)
            elif scores[i][j] == "1":
                ow += wins[j] / (games[j] - 1)
        owps.append(ow/len(oppos[i]))
#    print owps
    oowps = []
    for i in range(teams):
        oow = 0
        for j in oppos[i]:
            oow += owps[j]
        oowps.append(oow/len(oppos[i]))
    points =[]
    for i in range(teams):
        points.append(0.25*wps[i] + 0.5* owps[i] + 0.25* oowps[i] )
    return points

def main():
    input = sys.argv[1]
    output = sys.argv[2]

    f = open(input)
    fo = open(output,"w")
    cases = int(f.readline().strip())
    for i in range(cases):
        outs = []
        teams = int(f.readline().strip())
        scores = []
        for t in range(teams):
            scores.append(f.readline().strip())
        outs.append("Case #%d:"%(i+1)+"\n")
        for point in getRPI(teams,scores):
            outs.append(str(point)+"\n")
        for out in outs:
            print out,
            fo.write(out)
    fo.close()
    f.close()
if __name__ == '__main__':
    main()
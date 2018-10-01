# -*- coding: utf-8 -*-
from __future__ import division
fname = "A-large"
fin = open(fname+".in","r")
fout = open(fname+".out","w")
def gcj_read():
  linestr = fin.readline().strip()
  return [int(numb) for numb in linestr.split()]

numcases = gcj_read()[0]

symbols = {'1':True, '0':False, '.':None}

def wp(teamresults):
    played = sum(1 for x in teamresults if x is not None)
    won = sum(1 for x in teamresults if x)
    return won/played
    
def owp(results, teamno):
    teamresults = results[teamno]
    totalwp, n = 0.0, 0
    for i, x in enumerate(teamresults):
        if x is None:
            continue
        opp_results = results[i]
        totalwp += wp(opp_results[:teamno] + opp_results[teamno+1:])
        n += 1
    return totalwp/n
    
def oowp(owps, results, teamno):
    teamresults = results[teamno]
    totalowp, n = 0.0, 0
    for i, x in enumerate(teamresults):
        if x is None:
            continue
        totalowp += owps[i]
        n += 1
    return totalowp/n
        
for caseno in range(numcases):
    N = gcj_read()[0]
    results = [[symbols[x] for x in fin.readline().strip()] for _ in range(N)]
    
    team_wps = [wp(r) for r in results]
    team_owps = [owp(results, i) for i in range(N)]
    team_oowps = [oowp(team_owps, results, i) for i in range(N)]
    
    fout.write("Case #"+str(caseno+1)+":\n")
    for twp, towp, toowp in zip(team_wps, team_owps, team_oowps):
        RPI = (0.25*twp) + (0.5*towp) + (0.25*toowp)
        fout.write(str(RPI) + "\n")
    

fin.close()
fout.close()

#!/usr/bin/env python

import os, sys
import codejam
import fractions

def rpi(testcase):
    if len(testcase) < 2 or len(testcase) != 1+int(testcase[0]):
        raise RuntimeError, "Oops, we got a bad testcase!"
    nlines = int(testcase[0])
    teams = []
    for i in range(nlines):
        thistest = testcase[i+1].strip()
        if len(thistest) != nlines:
            raise RuntimeError, "Oops, we got a bad testline!"
        teamsplayed = []
        teamsbeaten = []
        for c in range(nlines):
            if thistest[c] == '1':
                teamsplayed.append(c)
                teamsbeaten.append(c)
            elif thistest[c] == '0':
                teamsplayed.append(c)
            elif thistest[c] == '.':
                pass
        teams.append( (teamsplayed, teamsbeaten) )

    wps = []
    for i in range(len(teams)):
        (teamsplayed, teamsbeaten) = teams[i]
        wps.append(fractions.Fraction(len(teamsbeaten), len(teamsplayed)))

    owps = []
    for i in range(len(teams)):
        (teamsplayed, teamsbeaten) = teams[i]
        owp = fractions.Fraction(0,1)
        for j in teamsplayed:
            (otplayed, otbeaten) = teams[j]
            oplayed = len(otplayed)-1
            obeaten = len(otbeaten)
            if j not in teamsbeaten:
                obeaten -= 1
            owp += fractions.Fraction(obeaten, oplayed)
        owps.append(owp*fractions.Fraction(1, len(teamsplayed)))

    oowps = []
    for i in range(nlines):
        (played, won) = teams[i]
        oowp = fractions.Fraction(0,1)
        for j in played:
            oowp += owps[j]
        oowps.append(oowp*fractions.Fraction(1, len(played)))

    rpis = []
    for i in range(nlines):
        rpis.append(wps[i]*fractions.Fraction(1,4)+owps[i]*fractions.Fraction(1,2)+oowps[i]*fractions.Fraction(1,4))

    return "\n" +"\n".join([("%8g" % i).strip() for i in rpis])

def extra_lines(lines):
    return int(lines[0])

if __name__ == "__main__":
    codejam.main(sys.argv[1:], rpi, 1, extra_lines=extra_lines)

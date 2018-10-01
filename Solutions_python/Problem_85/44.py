# -*- coding: utf-8 -*-
"""
Created on Sat May 07 10:07:30 2011

@author: Shahar
"""

import operator as op
from numpy import argsort

def B(inpfile):
    fin = open(inpfile, 'r')
    fout = open(inpfile+'.out', 'w')
    CNT = int(fin.readline())
    for iCNT in xrange(CNT):
        Case = map(int, fin.readline().rstrip('\n').split(' '))
        Boosters = Case[0]
        BuildTime = Case[1]
        nStars = Case[2]
        nDistances = Case[3]
        Distances = Case[4:]
        DistanceOccur = nStars / nDistances
        DistanceRem = nStars % nDistances

        SumDistances = reduce(op.add, Distances)
        Useless = BuildTime / (2*SumDistances)
        UselessRem = BuildTime % (2*SumDistances)
        UslessRound = 0

        Extra = 0
        
        Occur = Distances[:]
        TotalDistance = 0
        for iD in xrange(len(Occur)) :
            Occur[iD] = DistanceOccur - Useless
            TotalDistance += DistanceOccur*Distances[iD]
            if iD < DistanceRem :
                Occur[iD] +=  1
                TotalDistance += Distances[iD]
            if UslessRound  < UselessRem :
                if Occur[iD] > 0 and UslessRound + 2*Distances[iD] > UselessRem :
                    Extra = (UslessRound + 2*Distances[iD] - UselessRem)/2
                Occur[iD] -=  1
            UslessRound += 2*Distances[iD]
            Occur[iD] = max(Occur[iD], 0)
        
        if Extra > 0 :
            Distances.append(Extra)
            Occur.append(1)
        
        BoostersLeft = Boosters
        TotalTime = min(BuildTime, TotalDistance*2)
        Order = argsort(Distances)[::-1]
        for iO in xrange(len(Order)) :
            iD = Order[iO]
            AvailBoosters = min(BoostersLeft, Occur[iD])
            Mult = AvailBoosters+2*(Occur[iD]-AvailBoosters)
            TotalTime += Mult*Distances[iD]
            BoostersLeft -= AvailBoosters
        
        text = 'Case #' + str(iCNT+1) + ': ' + str(TotalTime)
        print text
        fout.write(text + '\n')

if __name__ == "__main__":
    #B(sys.argv[1]);
    #B('..\\test\\B-test.in');
    #B('..\\test\\B-small-attempt0.in');
    #B('..\\test\\B-small-attempt1.in');
    #B('..\\test\\B-small-attempt2.in');
    B('..\\test\\B-large.in');

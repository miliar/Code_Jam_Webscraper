from numpy import *

def Cost(a,b):                 # Double the initial cost
    d = b-a;
    return ((2*N+1-d)*d)/2
    


def Solve(cost, onoff):
    newCost = cost;

    while len(onoff) != 0:
#        if onoff[0][2] != 0:
#            onoff[0][1] -= onoff[0][2];     # Anybody getting off at stop 1
#            onoff[0][2] = 0;
#        if onoff[-1][1] != 0:
#            onoff[-1][2] -= onoff[0][1];    # Anybody getting on at stop N
#            onoff[-1][1] = 0;

#        print '1b', onoff

        while (len(onoff) > 0) and (onoff[0][1] == onoff[0][2]):
            onoff.pop(0);
        while (len(onoff) > 0) and (onoff[-1][1] == onoff[-1][2]):
            onoff.pop(-1)
        if len(onoff) <= 1:
            return newCost
        
#        print '1c', onoff

        L = len(onoff)
        OnTrain = [0]*(L-1);
        for i in range(L-1):
            OnTrain[i] = OnTrain[i-1] + onoff[i][1] - onoff[i][2];
            if OnTrain[i] == 0:
                return newCost + Solve(0, onoff[:i+1]) + Solve(0, onoff[i+1:]);

        NP = min( (onoff[0][1]-onoff[0][2]), (onoff[-1][2]-onoff[-1][1]), min(OnTrain) );

        newCost += NP*Cost(onoff[0][0], onoff[-1][0]);

        onoff[0][1] -= NP;
        onoff[-1][2] -= NP;

    return newCost

T = int(raw_input());
for q in range(1, T+1):
    [N,M] = map(int, raw_input().split());
#    print N,M
    Ival = 0;
    DATA =  [];

#   Store station number, #on's, #off's
    Station = [];

    for i in range(M):
        [o,e,p] = map(int, raw_input().split())
        Ival += Cost(o,e)*p;            # Initial cost

        DATA.append( [o,e,p] );
        Station.append(o);
        Station.append(e);
    Station = list(set(Station));
    Station.sort()                      # List of stations in order
    L = len(Station);
    
    OnOffs = [];
    for i in range(L):
        OnOffs.append( [Station[i], 0,0] );
    for row in DATA:
        for i in range(L):
            if Station[i] == row[0]:
              OnOffs[i][1] += row[2];
            if Station[i] == row[1]:
              OnOffs[i][2] += row[2];
    
    Fval = Solve(0, OnOffs)
    ANS = (Ival-Fval)%1000002013
#    print Ival, Fval

    print "Case #%d: %d" % (q, ANS)

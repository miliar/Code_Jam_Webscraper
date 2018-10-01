import sys
from fractions import gcd
cin = sys.stdin.readline


def solve(teams):
    #print teams
    N = len(teams)
    WP = [float(team.count('1')) / (team.count('0') + team.count('1'))
          for team in teams]
    OWP = []
    for q, team in enumerate(teams):
        tt = []
        for i, c in enumerate(team):
            #print i,c
            if c != '.':
                a,b = 0,0
                for j, cc in enumerate(teams[i]):
                    #print j,cc
                    if j != q:
                        if cc == '1':
                            a += 1
                            b += 1
                        elif cc == '0':
                            b += 1
                tt.append(float(a) / b)
        OWP.append(sum(tt) / len(tt))
    OOWP = []
    for q, team in enumerate(teams):
        tt = []
        for i, c in enumerate(team):
            if c != '.':
                tt.append(OWP[i])
        OOWP.append(sum(tt) / len(tt))
    ans = [0.25*A + 0.5 * B + 0.25 * C for (A,B,C) in zip(WP,OWP,OOWP)]
    return '\n'.join(['%.12f'%i for i in ans])
                                


if __name__ == '__main__':
    T = int(cin())
    for cnum in xrange(T):
        N = int(cin())
        print "Case #{0}:".format(cnum+1)
        print solve([cin().strip() for i in xrange(N)])
                    
            
        
    

from numpy import *

FILE = open("A-large.in","r");


def Check(Board, c):
    # Left-Right;
    for x in range(N):
        n = int(Board[x][0] == c);
        for y in range(1,N):
            if (Board[x][y] == c):
                n += 1;
                if (n == K):
#                    print (x,y), "Horizontal", c, n
                    return True;
            else:
                n = 0;

    for y in range(N):
        n = int(Board[0][y] == c);
        for x in range(1,N):
            if (Board[x][y] == c):
                n += 1;
                if (n == K):
#                    print (x,y), "Vertical", c, n
                    return True;
            else:
                n = 0;

    for x in range(N-K+1):
        for y in range(N-K+1):
            n = int(Board[x][y] == c);
            for q in range(1,K):
                n += int(Board[x+q][y+q] == c);
                if n == K:
#                    print "Diagonal", (x,y)
                    return True
                    
    for x in range(K-1,N):
        for y in range(N-K+1):
            n = int(Board[x][y] == c);
            for q in range(1,K):
                n += int(Board[x-q][y+q] == c);
                if n == K:
#                    print "Diagonal", (x,y)
                    return True

                
    return False;

def Rotate(data):
    Good = [];
    for q in range(N):
        if (data[q] != '.'):
            Good.append(data[q]);
    Ret = [];
    for q in range(N-len(Good)):
        Ret.append('.');
    Ret = Ret+Good;
#    print Ret;
    return Ret;


def Solve(N, K):
    DATA = [];                  DROP = [];
    for a in range(N):
        DATA.append([]);
        DROP.append([]);
        for b in range(N):
            DATA[a].append('.');
            DROP[a].append('.');
            
#    print N,K
    for a in range(N):
        Line = FILE.readline();
        for b in range(N):
            DATA[a][b] = Line[b];
        Column = Rotate(Line);
        for d in range(N):
            DROP[d][N-1-a] = Column[d];
    
#    for b in range(N):
#        for a in range(N-1,-1,-1):
#            print DATA[a][b],;
#        print "   ",;
#        for a in range(N):
#            print DROP[b][a],;
#        print " ";
#        
    Red = Check(DROP,'R');
    Blue= Check(DROP,'B');
    if (Red and Blue):
        return "Both";
    if (Red):
        return "Red";
    if (Blue):
        return "Blue";
    return "Neither";


T = int(FILE.readline());
for k in range(T):          # Each of the N cases:
    print "Case #%d:" %(k+1),
    [N,K] = map( int, FILE.readline().split() );
    print Solve(N,K);

#-------------------------------------------------------------------------------
# Dancing with googlers
#-------------------------------------------------------------------------------
import io;

# scores (x,y,z)
# 0 <= x,y,z <= 10
# suprise =^= max(x,y,z) - min (x,y,z) == 2
# impossible =^= max(x,y,z) - min (x,y,z) > 2

# point for googler = x+y+z

def isSuprise(score):
    if ((max(score) - min(score)) == 2):
        return True
    else:
        return False;

#def howManySuprisesNeededMin(totalScore,P):


#def couldHaveGetAtLeastP(totals,suprisingScores,P):


sumsMap = dict();

def prepareCache():
    """min score"""
    for a in range(0,11):
        for b in range(a,a+3):
            for c in range(a,a+3):
                sum = a+b+c;
                if not sum in sumsMap:
                    sumsMap[sum] = [];
                sumsMap[sum].append((a,b,c,isSuprise((a,b,c))))

def isPossibleAtLeastP(P,totals):
    Found = False;
    WithSuprise = True;
    matchingScoresNoSuprise = [];
    matchingScoresWithSuprise = [];
    for grade in sumsMap[totals]:
        (a,b,c,isSuprise) = grade
        if (a>=P) or (b>=P) or (c>=P):
            Found = True
            if not isSuprise:
                WithSuprise = False
                break

    return (Found,WithSuprise)

def parseLine(line):
    values=line.split();
    N = int(values[0]);
    S = int(values[1]);
    P = int(values[2]);
    scores = [];
    for i in range(3,3+N):
        scores.append(int(values[i]))

    return (N,S,P,scores)

def calculate(N,S,P,scores):
    numOf = 0;
    SuprisesAllowed = S;
    for score in scores:
        isPossible=isPossibleAtLeastP(P,score);
        if isPossible[0]:
            if not isPossible[1]:
                numOf += 1
            elif SuprisesAllowed > 0:
                numOf += 1
                SuprisesAllowed -= 1
    return numOf

def main():
    prepareCache()
    fd = open( "input.txt" )
    numoflines = int(fd.readline())

    for i in range (1,numoflines+1):
        (N,S,P,scores) = parseLine(fd.readline())
        result = calculate(N,S,P,scores)
        print ("Case #%d: %d"%(i,result))
    pass

if __name__ == '__main__':
    main()
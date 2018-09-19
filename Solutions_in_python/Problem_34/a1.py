
def parse( case ):
    pcase = [];
    i = 0;
    inb = False;
    case = case[:-1];
    for c in case:
        if( c == '(' ):
          pcase.append( [] );
          inb = True;
        elif( c == ')' ):
            i += 1;
            inb = False;
        else:            
            if not inb:
                i += 1;
                pcase.append( c );
            else:
                pcase[i].append( c );
    return pcase;


def match( case, word ):
    i = 0;
    word = word[:-1];
    for c in word:
        if not c in case[i]:
            return False;
        i += 1;
    return True;


rawdata = open("A-large.in").readlines();

L, D, N = rawdata[0][:-1].split(" ");

L = int(L);
D = int(D);
N = int(N);

words = rawdata[1:D+1];

rawcases = rawdata[D+1:D+N+1];

i = 1;
for rawcase in rawcases:
    case = parse( rawcase );
    matches = 0;
    for word in words:
        if match( case, word ):
            matches += 1;
    print "Case #" + str(i) + ": " + str(matches);
    i += 1;

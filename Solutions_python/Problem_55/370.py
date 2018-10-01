def doProb(fname, ofname):
    #do problem 3 given a file name
    f = open(fname, 'r');
    T = int(f.readline());
    output = ['Case #' + str(i) + ': '+ \
              str(solve([int(j) for j in f.readline().split()], [int(j) for j in f.readline().split()])) + \
              '\n' for i in range(1,T+1)];
    f.close();
    of = open(ofname, 'w');
    of.writelines(output);
    of.close();
    

def solve(x,g):
    (R,k,N) = x; #unpack the input
    (np, cash) = getParms(k,g);
    cur = 0;
    tot = 0;
    for i in range(R):
        tot += cash[cur];
        cur = np[cur];
    return tot;
    

def getParms(k,g):
    N= len(g);
    
    #special case, all passengers fit in the roller coaster:
    if(sum(g) <= k):
        np = range(N);
        cash = [sum(g)]*N;
        return (np, cash);
    
    #other cases
    np = [];
    cash = [];
    for i in range(N):
        tot = g[i];
        j = i;
        while(tot <= k):
            j = (j+1)%N;
            tot += g[j];
        tot -= g[j];
        np.append(j);
        cash.append(tot);
    
    return (np, cash);


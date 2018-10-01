import sys, itertools

with open(sys.argv[1]) as f:
    for x in range(int(f.readline().strip())):
        P,Q = (int(x) for x in f.readline().strip().split())
        torelease = [int(x)-1 for x in f.readline().strip().split()]
        prisoners = [1 for x in range(P)]
        minnumber = 500
        for order in itertools.permutations(torelease):
            cost = 0
            prisoners = [1 for x in range(P)]
            for prisoner in order:
                prisoners[prisoner] = 0
                n = 1
                while True:
                    if prisoner-n > -1 and prisoners[prisoner-n] == 1:
                        cost +=1
                        n+=1
                    else:
                        break
                n = 1
                while True:
                    if prisoner+n < P and prisoners[prisoner+n] == 1:
                        cost +=1
                        n+=1
                    else:
                        break


            minnumber = min(minnumber,cost)
            
        print("Case #",str(x+1),": ",minnumber,sep="")

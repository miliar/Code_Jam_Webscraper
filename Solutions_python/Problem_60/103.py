#!/usr/bin/python

import sys

def flock(X, V, B, T, K):
#    print("N,K,T,B = %d %d %f %f" %(len(X),K,T,B))
#    print("X=" +str(X) + "\nV="+ str(V))
    # First transform each hen in time to arrival
    H = [ (B-x)/v for (x,v) in zip(X,V) ]
#    print("Hens=" + str(H))
    c = 0
    # Count from end to beggining
    i=len(H)-1
    Krest = K
    

    for i in xrange(len(H)-1, -1, -1):
        if H[i]<=T:
            # This hen (And any that impact with it) will arrive on time
            Krest-=1
        else:
            # This hen is a blocker!!! All the hen after must be swapped
            c += Krest
        if Krest==0:
            break

    if Krest==0:
        return c
    else:
        return "IMPOSSIBLE"

def main(nameIn, nameOut):
    """Read form the input and write thr Case #:"""

    
    fI = open(nameIn, 'r')
    fO = open(nameOut, 'w')

    # First line is the number of cases
    l = fI.readline()
    Nl = int(l[0:-1])

    i=0
    step = 0
    for line in fI:
        line = line.strip() # This will remove the \n also
        if len(line)==0:
            continue
        
        if i>Nl:
            break

        if step==0:
            N,K,B,T = line.split()
            N = int(N)
            K = int(K)
            T = float(T)
            B = float(B)
            step += 1
        elif step==1:
            X = [ float(x) for x in line.split() ]
            step += 1
        elif step==2:
            i += 1
            V = [ float(v) for v in line.split() ]
            sw = flock(X, V, B, T, K)
            fO.write("Case #" + str(i) + ": " + str(sw) + "\n")
            step = 0
            
    fI.close()
    fO.close()


if __name__ == "__main__":
    if len(sys.argv)<3:
        print("Usage: " + sys.argv[0] + " <file_in> <file_out>")
        exit(0)

    main(sys.argv[1], sys.argv[2])

    

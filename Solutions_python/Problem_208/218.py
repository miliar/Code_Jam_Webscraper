import sys
import numpy as np



if __name__ == "__main__":
    f = sys.stdin
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        if fn != '-':
            f = open(fn)

    t = int(f.readline())
    for _t in xrange(t):
        inp = np.array(f.readline().split(), 'int')

        n = inp[0]
        q = inp[1]

        E = np.array([0] * n)
        S = np.array([0] * n)

        for i in range(n):
            inp = np.array(f.readline().split(), 'int')
            E[i] = inp[0]
            S[i] = inp[1]

        D = []

        dist = np.array([0] * n)

        for i in range(n):
            inp = np.array(f.readline().split(), 'int')
            if(i+1<n):
                dist[i+1] = dist[i] + inp[i+1]
                D.append(inp[i+1])
                

        for i in range(q):
            inp = np.array(f.readline().split(), 'int')


        # print E
        # print S
        # print D

        T = np.array([10000000000000.] * n)
        T[0] = 0.
        for i in range(1,n):
            for j in range(i):
                ds = float(dist[i]-dist[j])
                # print(ds)
                if ds <= E[j]:
                    T[i] = min(T[i], T[j] + ds/S[j])
            # print(T[i])

        output = T[n-1]

        # output = solve_small(n, counts)
        
        print("CASE #{0}: {1}".format(_t+1, output))
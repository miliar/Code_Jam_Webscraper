import numpy as np

if __name__ == '__main__':
    T = int(raw_input())
    for t in xrange(T):
        N, M = [int(x) for x in raw_input().split()]
        X = np.zeros((N, M), dtype=np.int)
        for n in xrange(N):
            X[n,:] = [int(x) for x in raw_input().split()]

        col_max = np.max(X, axis=0)
        row_max = np.max(X, axis=1)

        bad = False
        for i in xrange(N):
            for j in xrange(M):
                if X[i,j] < col_max[j] and X[i, j] < row_max[i]:
                    bad = True
                    break
            if bad:
                break

        print 'Case #{}: {}'.format(t+1, 'NO' if bad else 'YES')

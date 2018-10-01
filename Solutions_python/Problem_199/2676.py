import sys

def solve(path):
    L = open(path, "rb").read().splitlines()
    t = 1
    for line in L[1:]:
        S, K = line.split()
        S = map(lambda x: x == '+', S)
        K = int(K)
        count = 0
        for i in xrange(len(S)-K+1):
            if not S[i]:
                count += 1
                for j in xrange(K):
                    S[i+j] = not(S[i+j])
        print "Case #%d:" % t,
        t += 1
        if not all(S):
            print "IMPOSSIBLE"
        else:
            print count

if __name__ == "__main__":
    solve(*sys.argv[1:])
            

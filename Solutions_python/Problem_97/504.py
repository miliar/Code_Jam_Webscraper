import sys

if __name__ == "__main__":
    
    T = int(sys.stdin.readline())

    for x in xrange(1, T+1):
        
        A, B = map(int, sys.stdin.readline().split())

        pairs = set()

        for n in xrange(A, B):
            n_str = str(n)
            perms = [int(p) for p in [n_str[idx:] + n_str[:idx] for idx in range(1, len(n_str))]]
            pairs.update( (n, m) for m in perms if m > n and m <= B )

        print("Case #%d: %d" % (x, len(pairs)))

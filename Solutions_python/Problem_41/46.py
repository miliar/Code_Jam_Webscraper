#!/usr/bin/python

if __name__ == '__main__':
    T = int(raw_input())
    for n in xrange(1, T + 1):
        N = raw_input()
        K = ''
        for i in xrange(len(N) - 1, 0, -1):
            if N[i] > N[i - 1]:
                K = N[:i - 1]
                K += min([d for d in N[i:] if d > N[i - 1]])
                K += ''.join(sorted(N[i - 1:].replace(K[-1], '', 1)))
                break
        if not K:
            K = min([d for d in N if d > '0'])
            K += '0'
            K += ''.join(sorted(N.replace(K[0], '', 1)))
        
        print "Case #%d: %s" % (n, K)


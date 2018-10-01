def ints():
    return map(int,raw_input().split())

def main():
    T, = ints()
    for case in xrange(1,T+1):
        N, = ints()
        xs = range(N)
        for k in xrange(N):
            xs[k] = raw_input().rfind("1")

        perms = 0
        bad = True
        while bad:
            bad = False
            L = len(xs)
            for k in xrange(L):
                if xs[k] > k+(N-L):
                    bad = True
                    for j in xrange(k+1,L):
                        if xs[j] <= k+(N-L): # good
                            perms += j-k
                            xs = xs[k:j]+xs[j+1:]
                            break
                    else:
                        raise "nathan is dumb"
                    break
                
        print "Case #%s: %s" % (case,perms)

main()

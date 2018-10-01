def isTidy(n):
    for i in xrange(len(n)-1):
        if n[i] > n[i+1]:
            return False
    return True

def reduce(n):
    for i in xrange(len(n)-1):
        if n[i] > n[i+1]:
            return n[:i] + str(int(n[i])-1) + ('9' * (len(n)-i-1))


if __name__ == "__main__":
    ncases = int(raw_input())

    for i in xrange(1, ncases+1):
        n = raw_input()
        while not isTidy(n):
            n = reduce(n)
        print "Case #{}: {}".format(i,int(n))

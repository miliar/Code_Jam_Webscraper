if __name__ == "__main__":
    ncases = int(raw_input())
    for i in xrange(1, ncases+1):
        s, n = raw_input().split()
        n = int(n)

        x = [0] * (len(s) - n + 1) 
        s = [0 if c == '+' else 1 for c in s] 
        x[0] = s[0]

        for j in xrange(1,len(s) -n +1):
            x[j] = (sum(x[max((0, j-n+1)) : j]) + s[j]) %2

        valid = True
        for j in xrange(-n+1, 0):
            if s[j] != sum(x[j:]) % 2:
                valid = False
                break

        if valid:
            print "Case #{}: {}".format(i, sum(x))
        else:
            print "Case #{}: IMPOSSIBLE".format(i)





#!/usr/bin/python

def gcd(a, b):
    if a:
        return gcd(b%a, a)
    return b

def main():
    c = int(raw_input())
    for i in range(c):
        x = raw_input().split(' ')
        n = x[0]
        t = x[1:]
        t = [int(a) for a in t]
        t.sort()
        d = []
        for j in range(len(t)-1):
            d.append(t[j+1]-t[j])
        g = d[0]
        for j in range(len(d)):
            g = gcd(g, d[j])

        
        print "Case #" + str(i+1) + ": " + str((g - t[0])%g)


if __name__ == '__main__':
    main()

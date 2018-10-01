#!/usr/bin/env python

def Solve(a, b, m, h):
    d = 0
    res = 0
    arr = [-1.0]*b
    arr[0] = 0.0

    for i in xrange(b-1):
        agg = 0.0
        for j in xrange(i+1, b):
            if h[i][0] >= m[j-1][j]+agg:
                if arr[j] < 0.0 or arr[j] > arr[i] + float(m[j-1][j]+agg)/h[i][1]:
                    arr[j] = arr[i] + float(m[j-1][j]+agg)/h[i][1]
                agg += m[j-1][j]
            else:
                break
    return arr[b-1]

def main():
    t = int(raw_input())
    for i in xrange(t):
        p = raw_input().rstrip().split(" ")
        n = int(p[0])
        q = int(p[1])
        horses = []
        for j in xrange(n):
            p = raw_input().rstrip().split(" ")
            horses.append((int(p[0]), int(p[1])))
        m = []
        for j in xrange(n):
            p = raw_input().rstrip().split(" ")
            m.append([int(t) for t in p])
        qs = []
        for j in xrange(q):
            p = raw_input().rstrip().split(" ")
            qs.append((int(p[0]), int(p[1])))


        print "Case #" + str(i+1) +": " + " ".join([str(Solve(t[0], t[1], m, horses)) for t in qs])

if __name__ == "__main__":
    main()

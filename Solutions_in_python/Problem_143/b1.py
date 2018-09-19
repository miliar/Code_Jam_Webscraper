t = int(input())

def solve(a,b,k):
    c = 0
    ra = 0
    rb = 0
    while ra < a:
        if (ra & rb) < k:
            c +=1
        rb += 1
        if rb >= b:
            rb = 0
            ra += 1
    return c

for case in range(t):
    a,b,k = [int(i) for i in input().split(' ')]

    print ("Case #%s: %s" % (case+1, solve(a,b,k)))

def final_answer(n):
    x = n//2
    if n % 2 == 1:
        return "{} {}".format(x, x)
    return "{} {}".format(x, max(x-1, 0))

def solve(n, k):
    d = {n:1}
    # n is the highest key we have
    m = 1 # m is the number of instance of the highest key we have

    while k > m:
        #print d
        del d[n]
        x = n//2
        if n % 2 == 1:
            if x in d:
                d[x] = d[x] + m * 2
            else:
                d[x] = m * 2                
        else:
            if x in d:
                d[x] = d[x] + m
            else:
                d[x] = m
            if x-1 in d:
                d[x-1] = d[x-1] + m
            else:
                d[x-1] = m
                
        k = k - m
        n = max(d.keys())
        m = d[n]

    #print d, n
    return final_answer(n)

t = int(raw_input())
for i in xrange(1, t + 1):
    n, k = [int(x) for x in raw_input().split(" ")]
    print "Case #{}: {}".format(i, solve(n, k))

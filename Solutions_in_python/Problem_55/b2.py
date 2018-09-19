import sys

def foo():
    line = sys.stdin.readline()
    R, k, N = [int(x) for x in line.split()]
    g = [int(x) for x in sys.stdin.readline().split()]

    if(sum(g) <= k):
        return R * sum(g)
        

    res = []
    res2 = {}

    s = 0
    while 1:
        if s in res2:
            break
        
        g2 = g[s:] + g[:s]
        #print s, g2
        t = 0
        for i in range(len(g2)):
            if t + g2[i] > k:
                res.append(t)
                res2[s] = len(res)-1
                s = (s + i) % N
                break
            t += g2[i]

    if R < len(res):
        return sum(res[:R])

    start = res2[s]
    circle = len(res) - res2[s]
    circle_count = (R - start) // circle
    other = (R - start) % circle
    return sum(res[:start]) + sum(res[start:]) * circle_count + sum(res[start:start+other])
        

def main():
    n = int(sys.stdin.readline())
    for i in range(n):
        print "Case #%s: %s" % (i+1, foo())


if __name__ == '__main__':
    main()

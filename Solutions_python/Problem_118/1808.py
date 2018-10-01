pals = [1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 10000200001, 10221412201, 12102420121, 12345654321, 40000800004, 1000002000001, 1002003002001, 1004006004001, 1020304030201, 1022325232201, 1024348434201, 1210024200121, 1212225222121, 1214428244121, 1232346432321, 1234567654321, 4000008000004, 4004009004004]

T = int(raw_input())

for i in xrange(1, T+1):
    a, b = [int(e) for e in raw_input().split(' ')]
    
    count = 0
    for n in pals:
        if n < a:
            continue
        if n > b:
            break
        count += 1

    print "Case #%d: %d" % (i, count)

""" What follows is my original code. I used it to precompute the set.

def pal(s):
    return all(s[i] == s[len(s) - i - 1] for i in xrange(len(s) / 2 + 1))

T = int(raw_input())

for i in xrange(T):
    a, b = [int(e) for e in raw_input().split(' ')]
    tot = set()
    
    stop = int(b**.5) + 2
    while stop ** 2 > b:
        stop -= 1
    
    start = int(a**.5)
    while start**2 < a:
        start += 1
    
    count = 0
    for j in xrange(start, stop + 1):
        if pal(str(j)) and pal(str(j**2)):
            tot.add(j**2)
            count += 1
        j += 1
    print "Case %d: %d" % (i, count)
    tot = list(tot)
    tot.sort()
    print tot
"""

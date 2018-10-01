import sys

#f= open('A-TEST')
f = open(sys.argv[1])
T = int(f.readline())



vowels = ['a','e','i','o','u']

for case in range(T):
    str, N = f.readline().split(' ')
    N = int(N)
    l = len(str)
    letters = list(str)
    ss = []
    occs = set()
    ii = 0
    while ii < l:
        jj = 0
        while(letters[ii+jj] not in vowels):
            jj = jj + 1
            if ii + jj >= l:
                break
        if jj >= N:
            ss.append([int(ii),int(jj)])
        ii = ii + jj + 1
    #print str, ss
    for items in ss:
        for kk in range(items[0]+1+items[1]-N):
            for hh in range(max(kk+N-1,items[0]+N-1),l):
                occs.add((kk,hh+1))
    print "Case #%d: %d" % ((case+1), len(occs))






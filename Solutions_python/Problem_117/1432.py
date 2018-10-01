"""B
   Google CodeJam 2013
"""

from datetime import datetime
from collections import deque


def routine(N, M, s, s_row, s_col):
    def getnext():
        #returns next smallest (h,r,c)
        x = None
        while s_row:
            x = min([min(s_row[sr]) for sr in s_row])
            if x[2] not in s_col:
                s_row[x[1]].popleft()  #purge dead refs
                if not s_row[x[1]]:
                    del s_row[x[1]]  #nothing's left
                x = None
            if x:
                return x
        while s_col:
            x = min([min(s_col[sc]) for sc in s_col])
            if x[1] not in s_row:  #pointless test - we only get here if s_row is empty
                s_col[x[2]].popleft()  #purge dead refs
                if not s_col[x[2]]:
                    del s_col[x[2]]  #nothing's left
                x = None
            if x:
                return x
        return x
        
    sq = getnext()
    while sq:
        #flood/fail
        #print sq, s[sq[1]][sq[2]]
        flood = False
        #flood row, if it still exists
        if sq[1] in s_row:
            for c in xrange(M):
                if c == sq[2]:
                    continue   #skip self compare
                if c in s_col:
                    try:
                        #print "row compare (", sq[1], c, ")", s[sq[1]][c] , sq[0]
                        if s[sq[1]][c] > sq[0]:
                            break
                    except KeyError:
                        pass  #already discounted row/col - we can assume it was same/lower
            else:
                #print "del row",sq[1]
                del s_row[sq[1]]
                flood = True
        #flood col, if it still exists
        if sq[2] in s_col:
            for r in xrange(N):
                if r == sq[1]:
                    continue   #skip self compare
                if r in s_row:
                    try:
                        #print "col compare (", r, sq[2], ")", s[r][sq[2]] , sq[0]
                        if s[r][sq[2]] > sq[0]:
                            break
                    except KeyError:
                        pass  #already discounted row/col - we can assume it was same/lower
            else:
                #print "del col",sq[2]
                del s_col[sq[2]]
                flood = True
        
        if not flood:  #one was sealed in
            return "NO"
            
        sq = getnext()
    
    return "YES"  #all free and none remain

if __name__ == '__main__':
    filename = "B-large"  #small-attempt1"  #B-large
    f = open(filename + ".in")
    fo = open(filename + ".out", "w")

    print datetime.now()

    c = int(f.readline().strip())
    print c, "cases"
    for case in xrange(c):
        N, M = [int(x) for x in f.readline().split()]
        s = dict.fromkeys(xrange(N))
        s_row = dict.fromkeys(xrange(N), deque())
        s_col = dict.fromkeys(xrange(M), deque())
        for row in xrange(N):
            row_s = f.readline().split()
            s[row] = dict.fromkeys(xrange(M))
            for col, h in enumerate(row_s):
                s[row][col] = int(h)
            s_row[row] = deque(sorted([(s[row][c], row, c) for c in xrange(M)]))
        for col in xrange(M):
            s_col[col] = deque(sorted([(s[r][col], r, col) for r in xrange(N)]))
        
        
        print N,'x',M

        print >>fo, "Case #%d: %s" % (case+1, routine(N, M, s, s_row, s_col))

    fo.close()
    f.close()
    print datetime.now()

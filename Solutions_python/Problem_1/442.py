"""Saving the universe test 1 
   Google CodeJam 2008
"""

from datetime import datetime, timedelta

def routine(engines, querys):
    #print len(engines), len(querys)
    remaining = engines[:]
    switches = 0
    for query in querys:
        if query in remaining:
            remaining.remove(query)
    
        if not remaining:
            #need to switch and reload
            print "\tswitching at", query, "after sending to", query
            remaining = engines[:]
            remaining.remove(query)  #remove self
            switches += 1                   
                
    #print "remaining:", remaining
    #print "switches:", switches
    return switches


if __name__ == '__main__':
    filename = "A-large"
    f = open(filename + ".in")
    fo = open(filename + ".out", "w")

    n = int(f.readline())
    print n, "cases"
    for i in range(n):
        print "Case", i+1
        enginen = int(f.readline())        
        engines = []
        for engine in range(enginen):
            engines.append(f.readline().strip('\n'))

        queryn = int(f.readline())        
        querys = []
        for query in range(queryn):
            querys.append(f.readline().rstrip('\n'))

        print >>fo, "Case #%d: %s" % (i+1, routine(engines, querys))
        print

    fo.close()
    f.close()

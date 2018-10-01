import sys

     
numcases = int(sys.stdin.readline())
for casenumber in xrange(1,numcases+1):
    line = sys.stdin.readline().rstrip("\r\n")
    n = int( line )    
    
    line = sys.stdin.readline().rstrip("\r\n")
    line_elems = line.split(" ")

    items = sorted( [int(x) for x in line_elems] )
    
    score = reduce(lambda x,y: x^y, items)
    
    result = None
    if score != 0:
        result = "NO"
    else:
        result = sum(items[1:])

    print "Case #%d: %s" % (casenumber, result)


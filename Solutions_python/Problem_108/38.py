import sys




def solve(data,dist):
    cache = {}
    def f(vine, height):
        # print "looking at", vine, height
        if dist - data[vine][0] <= height:
            #print "got it!"
            return True
        key = (vine, height)
        try:
            return cache[key]
        except KeyError:
            pass

        cache[key] = False
        for i in xrange(len(data)):
            if i == vine: continue
            v, h = data[i]
            # can swing to vine
            diff = abs(v-data[vine][0])
            # print v,h,diff,vine, height, i
            if abs(diff) <= height:
                # print "can swing from", vine, "to", i, diff
                if f(i, min(h, diff)):
                    cache[key] = True
                    return True
        cache[key] = False
        return False
                
    if f(0, min(data[0][0], data[0][1])):
        return "YES"
    else:
        return "NO"


def main(lines):
    T = int(lines.next())
    for case in xrange(1,T+1):
        N = int(lines.next())
        data = []
        for ii in xrange(N):
            line = lines.next().strip()
            data.append(map(int, line.split()))
        dist = int(lines.next())
        
        r = solve(data, dist)
        print "Case #%d: %s" % (case, r)

# example output
"""
Case #1: YES
Case #2: NO
Case #3: YES
Case #4: NO
"""

if __name__ == "__main__":
    if sys.argv < 2:
        print "need a file name!"
    main(open(sys.argv[1]))
    # main(sys.stdin)
    




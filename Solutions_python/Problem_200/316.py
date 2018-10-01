

def findTidyNumber(n):
    new = map(int, list(n))
    
    found = -1
    for i in xrange(1, len(new)):
        if new[i] < new[i-1]:
            found = i
            # curr digit less than prev
            break
    if found != -1:
        for j in xrange(found, len(new)):
            new[j] = 9

        new[found-1] -= 1
        # back track to make sure it's decreasing
        for j in xrange(found-1, 0, -1):
            if new[j] < new[j-1]:
                new[j] = 9
                new[j-1] -= 1

    return "".join(map(str, new))


for case in xrange(input()):
    print "Case #%d: %d" % (case + 1, int(findTidyNumber(raw_input())))
import sys
import math

f = sys.stdin
cases = int(f.readline().strip())

# Given a stall gap of size n, return the maximal value of min(Ls, Rs)
def getMin(n):
    return int(math.ceil(float(n) / 2.0)) - 1

# Given a stall gap of size n, return the maximal value of max(Ls, Rs)
def getMax(n):
    return n / 2

# Consume given DB key, which means "occupy db[key] stalls"
def consume(db, n):
    numGroups = db[n]

    lowkey = getMin(n)
    hikey = getMax(n)
    
    # Create our new db entries for these groups
    if(lowkey not in db):
        db[lowkey] = 0
    if(hikey not in db):
        db[hikey] = 0

    # Split the stalls
    db[lowkey] += numGroups
    db[hikey] += numGroups

    del db[n]

for ii in range(cases):
    line = f.readline().strip()
    n = int(line.split(" ")[0])
    k = int(line.split(" ")[1])

    #print "getMin({0}): {1}".format(n,getMin(n))
    #print "getMax({0}): {1}".format(n,getMax(n))

    db = {n: 1}
    ans = [-1, -1]
    
    while (k > 0):
        target = max(db.keys())

        # If this group of stalls has enough for our last group,
        # return the coords for a group of this size
        if (k <= db[target]):
            ans[0] = getMax(target)
            ans[1] = getMin(target)
            k = 0
            break

        k -= db[target]
        consume(db, target)

    print "Case #{0}: {1} {2}".format(ii+1,ans[0],ans[1])

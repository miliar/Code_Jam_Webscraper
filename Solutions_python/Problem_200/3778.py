import sys

def is_tidy(n):

    if len(n) == 1:
        return True

    for i in range(len(n)-1,0,-1):
        if n[i] < n[i-1]:
            return False


    return True

with open(sys.argv[1]) as infile:
    numcases = int(next(infile))

    for casenum in range(1,numcases+1):
        startnum = int(next(infile).rstrip())

        while not is_tidy(str(startnum)):
            startnum -= 1

        print("Case #{}: {}".format(casenum, startnum) )



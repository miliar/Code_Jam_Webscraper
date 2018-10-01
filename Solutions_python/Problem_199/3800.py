def flip(bum):
    a = ""
    for achr in bum:
        if achr == "+":
            a += "-"
        else:
            a += "+"
    return a

def doit(pans, flsize):
    step = 0
    if "-" not in pans:
        return step
    while pans.index("-") < len(pans)-flsize+1 and "-" in pans:
        ind = pans.index("-")
        pans = pans[:ind] + flip(pans[ind:ind+flsize]) + pans[ind+flsize:]
        step +=1
        if "-" not in pans:
            return step
    return "IMPOSSIBLE"

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    n, m = [s for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    m = int(m)
    print "Case #{}: {}".format(i, doit(n,m))

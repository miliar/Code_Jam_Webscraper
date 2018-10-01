# Qualification Round
# Problem B

# Total time required to get X cookies if we buy
# n farms of cost C and production F
def getTime(n,C,F,X):
    t = 0.0
    for i in range(n):
        t += C/(2.0+float(i)*F)
    return t + X/(2.0+float(n)*F)

fname = "B-small-attempt0.in"
f = open(fname,"r")

T = int(f.readline())
for case in range(1,T+1):
    data = f.readline().split()
    C = float(data[0])
    F = float(data[1])
    X = float(data[2])
    time = getTime(0,C,F,X)
    n = 1
    while(True):
        newtime = getTime(n,C,F,X)
        if newtime > time: break
        else: time = newtime
        n += 1
    print "Case #%i: %f" % (case,time)
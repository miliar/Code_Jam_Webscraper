f = open("input")
input = f.read()
f.close()

lineno = 0
lines = input.split('\n')

def readline():
    global lines, lineno
    line = lines[lineno]
    lineno += 1
    return line

f = open("output", "w")
N = int(readline())
for i in range(N):
    S = int(readline())
    se = {}
    for j in range(S):
        se[readline()] = []
    Q = int(readline())
    for j in range(Q):
        se[readline()].append(j)
    max = -1
    switch = -1
    P = 0
    sel = ""
    while P<Q:
        for j in se:
            if (len(se[j])==0 or se[j][0]>max):# and j!=sel:
                if len(se[j])==0:
                    max = Q+1
                else:
                    max = se[j][0]
                    sel = j
        switch += 1
        for j in se:
            while len(se[j])>0 and se[j][0]<max:
                se[j] = se[j][1:]
        P = max
    if switch < 0:
        switch = 0
    print "Case #%d: %d"%(i+1,switch)
    f.write("Case #%d: %d\n"%(i+1,switch))
f.close()
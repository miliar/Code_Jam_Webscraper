f = open("welcome_in.txt")
data = f.read()
f.close()

data = data.split("\n")
n = int(data[0])
data = data[1:]

w = "welcome to code jam"



def case(c, ic, iw):
    global w, T, cache
    if ic == -1: return 0
    if iw == len(w): return 1
    if cache[ic][iw] == -1:
        t = 0    
        for i in xrange(ic, len(c)):
            if c[i] == w[iw]:
                t += case(c, i, iw+1)
        cache[ic][iw] = t
    return cache[ic][iw]

cache = []    
s = ""
for i in xrange(n):
    cache = []
    for j in xrange(len(data[i])):
        cache += [[-1] * len(w)]
        
    print float(i) / n * 100.0
    T = 0
    ans = case(data[i], data[i].find("w"), 0) % 10000
    ans = str(ans)
    ans = "0" * (4 - len(ans)) + ans
    s += "Case #%d: %s\n" % (i+1, ans)


print s

f = open("welcome_out.txt", "w")
f.write(s)
f.close()

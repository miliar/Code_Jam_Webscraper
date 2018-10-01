def isRecycledPair(n, m):
    ns = str(n)
    ms = str(m)
    for i in range(1, len(str(n))):
        s = ns[i:] + ns[0:i]
        if s == ms:
            return True

def getPairs(s):
    A = int(s[0])
    B = int(s[1])
    count = 0
    for n in range (A, B):
        for m in range (n + 1, B + 1):
            if isRecycledPair(n, m):
                count += 1
    return count

f = open("C-small-attempt0.in", "r")
w = open("out.txt", "w")

i = int(f.readline().rstrip())

for a in range (0, i):
    s = f.readline().rstrip()
    pairs = getPairs(s.split(' '))
    w.write("Case #" + str(a+1) + ": " + str(pairs) + "\n")

f.close()
w.close()

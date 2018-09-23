f = open("B-small-attempt0.in", "r")
f = f.readlines()

def isTidy(n):
    sn = str(n)
    inOrder = True
    for i in range(1, len(sn)):
        if sn[i] < sn[i-1]:
            inOrder = False
    return inOrder

for i in range(1, len(f)):
    s = f[i]
    n = int(s[:s.index("\n")]) if i < len(f)-1 else int(s)
    for j in range(n):
        if isTidy(n-j):
            print("CASE #"+str(i)+": "+str(n-j))
            break

inp = open('A-large.in', 'r')
out = open('A-large.out', 'w')

def single():
    return inp.readline().strip()

def mult():
    return inp.readline().strip().split()

def multint():
    x = inp.readline().strip().split()
    for a in range(len(x)):
        x[a] = int(x[a])
    return x

cases = int(inp.readline().strip())

def biggest(current, s, x):
    for a in reversed(s):
        if current + a <= x:
            return a
    return -1

for r in range(cases):

    a = multint()
    n = a[0]
    x = a[1]

    s = multint()
    s.sort()

    discs = 0

    while len(s) != 0:
        current = s[-1]
        s.pop()

        if len(s) != 0:
            t = biggest(current, s, x)

            if t != -1:
                s.remove(t)
        discs += 1

    print("Case #" + str(r+1) + ": " + str(discs))
    out.write("Case #" + str(r+1) + ": " + str(discs) + "\n") 
        

inp.flush()
out.flush()
inp.close()
out.close()

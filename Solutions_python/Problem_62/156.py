data = open('A-large.in').read().split()
data.reverse()
data = map(int, data)

T = data.pop()

for t in range(1, T + 1):
    n = data.pop()
    wires = []
    for i in range(n):
        a, b = data.pop(), data.pop()
        wires.append((a,b))
    
    sol = 0
    for i in range(n):
        for j in range(i+1, n):
            a1,b1 = wires[i]
            a2,b2 = wires[j]
            if (a1 > a2) != (b1 > b2):
                sol += 1
    print "Case #{0}: {1}".format(t, sol)
    
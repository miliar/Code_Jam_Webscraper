input = open('A-large.in','r')
output = open('A-large.out','w')
outstr = ""

T = int(input.readline())
for t in range(T):
    N = int(input.readline())
    wires = []
    for n in range(N):
        line = input.readline().split()
        wires.append((int(line[0]), int(line[1])))
    
    NW = 0
    for i in range(len(wires)-1):
        (S,E) = wires[i]
        for j in range(i+1, len(wires)):
            (s,e) = wires[j]
            if (S<s and E>e) or (S>s and E<e):
                NW += 1
    outstr += "Case #%d: %d\n"% (t+1, NW)
print outstr
output.write(outstr)
    
            


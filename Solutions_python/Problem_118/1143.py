from math import sqrt
f = open(r'C-small-attempt0.in', 'r')
g = open(r'outputC.out', 'w')
t = int(f.readline())
seen = set()
for i in range(1, t+1):
    g.write("Case #"+str(i)+": ")
    k = f.readline().split()
    counter = 0
    for j in range(int(k[0]), int(k[1])+1):
        if j in seen:
            counter += 1
        elif (str(j)==str(j)[::-1]):
            l = int(sqrt(j))
            s = str(l)
            if (l**2 == j) and (s == s[::-1]):
                seen.add(j)
                counter += 1
    g.write(str(counter)+"\n")
f.close()
g.close()
    

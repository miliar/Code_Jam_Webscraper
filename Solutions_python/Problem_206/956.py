f = open("input.in")

T = int(f.readline().replace("\n", ''))
o = open("output", "w")
for i in range(T):
    D, N = [int(v) for v in f.readline().replace("\n", '').split()]
    hrs = -1
    for k in range(N):
        Ki, Si = [int(v) for v in f.readline().replace("\n", '').split()]
        m = D - Ki
        t = m / Si
        if t > hrs:
            hrs = t
    
    o.write("Case #{}: {}\n".format(i+1, D/hrs))

o.close()
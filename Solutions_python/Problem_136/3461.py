fin = open("input.txt", "r")
fout = open("output.txt", "w")
T = int(fin.readline().strip())
for i in range(1, T + 1):
    c, f, x = map(float, fin.readline().split())
    time = 0
    v = 2
    while True:
        time += c / v
        t = c / f
        if c + v * t <= x:
            print("Case #", i, ": ", time + (x - c) / v, file = fout, sep = '')
            break
        else:
            v += f
fout.close()
fin = open("A-large (1).in")
fout = open("output.txt", "w")
t = int(fin.readline())
for q in range(t):
    d, n = map(int, fin.readline().split())
    k = [0] * n
    s = [0] * n
    for i in range(n):
        k[i], s[i] = map(int, fin.readline().split())
        k[i] = d - k[i]
    time = k[-1] / s[-1]
    for i in range(-2, -n - 1, -1):
        time = max(time, (k[i] / s[i]))
    print("Case #", q + 1, ": ", d / time, sep = '', file = fout)
fout.close()
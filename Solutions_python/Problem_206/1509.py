t = int(input())
f2 = open('output_2017.txt', 'w', encoding="utf-8")
def doit(d, n, h):
    r = 0
    for i in range(n):
        z = d - h[i][0]
        r = max(r, z / h[i][1])
    return d / r

for i in range(t):
    d, n = list(map(int, input().split(' ')))
    h = []
    for j in range(n):
        h.append(list(map(int, input().split(' '))))
    z = '%.6f' % doit(d, n, h)
    #print("Case #{}: {}".format(i+1, z))
    f2.write("Case #{}: {}\n".format(i+1, z))
f2.close()
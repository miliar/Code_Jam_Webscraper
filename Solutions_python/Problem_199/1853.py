fin = open("A-large.in")
fout = open("output.txt", "w")

t = int(fin.readline())
for i in range(t):
    s, k = fin.readline().split()
    k = int(k)
    n = len(s)
    s = list(s)
    x = 0
    for u in range(n):
        if s[u] == '+':
            continue
        else:
            x += 1
            if(u + k > n):
                break
            for j in range(u, u + k):
                if s[j] == '+':
                    s[j] = '-'
                else:
                    s[j] = '+'
    #print(s)
    if '-' in s:
        print("Case #", i + 1, ": IMPOSSIBLE", sep = "", file = fout)
    else:
        print("Case #", i + 1, ": ", x, sep = "", file = fout)
fout.close()
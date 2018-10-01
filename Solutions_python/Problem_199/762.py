fin = open("A-small-attempt0.in", 'r')
fout = open("A-small-attempt0.out", 'w')


n = int(fin.readline())
for ncase in range(1, n + 1):
    s, k = fin.readline().split()
    k = int(k)
    s = [0 if i == '-' else 1 for i in s]
    ss = len(s)
    ans = 0
    for i in range(ss):
        if (not s[i]):
            if (i + k > ss):
                print("Case #{}: IMPOSSIBLE".format(ncase), file=fout)
                break
            ans += 1
            for j in range(i, i + k):
                s[j] = (s[j] + 1) % 2
        #print(s)
    else:
        print("Case #{}: {}".format(ncase, ans), file=fout)

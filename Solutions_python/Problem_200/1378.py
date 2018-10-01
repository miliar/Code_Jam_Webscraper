t = int(raw_input())
ans = []
for h in range(t):
    y = raw_input()
    n = [int(x) for x in y]
    m = int(y)
    l = len(n)
    tidy = True
    for i in range(l-1):
        if n[i] > n[i+1]:
            tidy = False
            break
    count = m
    if ~tidy:
        i = l-1
        while i > 0:
            if n[i] < n[i-1]:
                j = i
                while j<l and n[j]!=9:
                    n[j] = 9
                    j+=1
                n[i-1] -= 1
            i -= 1
        count = int(''.join(map(str,n)))

    ans.append(count)

for h in range(t):
    print 'Case #'+str(h+1)+':', ans[h]

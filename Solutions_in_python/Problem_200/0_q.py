t = int(input())
for i in range(1, t + 1):
    s = str(input())
    ds = [int(s[j]) for j in range(len(s) - 1, -1, -1)]
    curr = ds[0]
    ans = [str(curr)]
    for j in range(1, len(ds)):
        if ds[j] > curr:
            ds[j] -= 1
            ans = ['9' for k in range(0, j)]
            ans.append(str(ds[j]))
            curr = ds[j]
        else:
            ans.append(str(ds[j]))
            curr = ds[j]
    print("Case #{}: {}".format(i, int(''.join(reversed(ans)))))

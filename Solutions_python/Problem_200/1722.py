t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    list_n = [int(s) for s in input().split(" ")]
    n = list_n[0]
    l = []
    k = -1
    for d in str(n):
        l.append(int(d))
    for w in range(0, len(l)-1):
        if l[w] > l[w+1]:
            k = w
            count = 0
            if k != 0:
                mult = w - 1
                while l[mult] == l[mult+1]:
                    count += 1
                    mult -= 1
            break
    if k != -1:
        l[k-count] = l[k-count]-1
        for j in range(k-count+1,len(l)):
            l[j] = 9
    final = 0
    for e in l:
        final = int(str(final) + str(e))
    print("Case #{}: {}".format(i, final))

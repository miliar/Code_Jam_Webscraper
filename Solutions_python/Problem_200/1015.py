for case in range(int(input())):
    n = list(input())
    idx = 0
    for i in range(len(n)):
        if i + 1 >= len(n):
            break
        if n[i] < n[i+1]:
            idx = i+1
        elif n[i] > n[i+1]:
            if idx == 0 and n[0] == '1':
                n = ['9' for _ in range(len(n) - 1)]
                break
            else:
                n[idx] = str(int(n[idx]) - 1)
                for j in range(idx + 1, len(n)):
                    n[j] = '9'
                break
    print("Case #{}: {}".format(case + 1, "".join(n)))

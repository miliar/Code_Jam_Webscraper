n_cases = int(input())

for i in range(1, n_cases + 1):
    n = int(input())
    n_s = list(map(int, list(str(n))))

    if len(n_s) == 1:
        print('Case #{}: {}'.format(i, n))
        continue

    for j in range(len(n_s) - 1):
        if n_s[j] > n_s[j+1]:
            if j == 0 or n_s[j] - 1 >= n_s[j-1]:
                n_s[j] -= 1
                for k in range(j+1, len(n_s)):
                    n_s[k] = 9
            else:
                for k in range(j-1, -1, -1):
                    if k == 0:
                        n_s[k] -= 1
                    elif n_s[k] - 1 >= n_s[k-1]:
                        n_s[k] -= 1
                        break
                    else:
                        n_s[k] = 9
                for k in range(j, len(n_s)):
                    n_s[k] = 9
            break
    res = int(''.join([str(s) for s in n_s]))
    print('Case #{}: {}'.format(i, res))

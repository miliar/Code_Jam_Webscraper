def last_tidy(k):
    s = list(map(int, str(k)))
    n = len(s)

    for i in range(-1,-n,-1):
        if s[i] < s[i-1]:
            s[i-1]-=1
            j = i
            while j != 0:
                s[j] = 9
                j+=1

    res = int(''.join(list(map(str, s))))

    return res


t = int(input())

for test_num in range(1, t+1):
    n = int(input())

    ans = last_tidy(n)

    print("Case #{}: {}".format(test_num, ans))

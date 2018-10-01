def solve(case_no):
    s = list(map(int, input()))

    tp = 0
    while tp != -1:
        tp = -1
        for i in range(1, len(s)):
            if s[i] < s[i-1]:
                tp = i
                break
        if tp != -1:
            s[i-1] -= 1
            for i in range(tp, len(s)):
                s[i] = 9

    ans = int(''.join(map(str, s)))
    print("Case #{}: {}".format(case_no, ans))

t = int(input())
for i in range(t):
    solve(i + 1)

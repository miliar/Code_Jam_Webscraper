def flip(s, k, i):
    for j in range(i, i + k):
        if s[j] == '-':
            s[j] = '+'
        else:
            s[j] = '-'
    return s


def solve(s, k, case):
    flipc = 0
    imp = False
    s = [c for c in s]
    while '-' in s:
        lim = len(s)
        sadc = 0
        flipped = False
        for i in range(lim):
            if s[i] == '-':
                if sadc == k - 1:
                    s = flip(s, k, i - sadc)
                    flipc += 1
                    flipped = True
                    sadc = 0
                    break
                else:
                    sadc += 1
            elif sadc > 0:
                if i - sadc + k <= lim:
                    s = flip(s, k, i - sadc)
                    flipped = True
                    flipc += 1
                    break
                sadc = 0
        if not flipped:
            imp = True
            break
        elif imp:
            break
        else:
            prev_state = s
    if imp:
        print("Case #{}: {}".format(case, 'IMPOSSIBLE'))
    else:
        print("Case #{}: {}".format(case, flipc))



with open('large.in', 'r') as fin:
    T = int(fin.readline().strip())
    for i in range(1, T + 1):
        S, K = (fin.readline().strip().split())
        K = int(K)
        solve(S, K, i)

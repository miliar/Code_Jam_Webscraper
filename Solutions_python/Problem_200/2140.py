def f(s):
    if s[0] == '0':
        return '9' * (len(s) - 1)
    for i in range(len(s) - 1):
        if s[i] > s[i + 1]:
            return f(s[:i] + chr(ord(s[i]) - 1) + '9' * (len(s) - i - 1))
    return s
for t in range(int(input())):
    print('Case #{}: {}'.format(t + 1, f(input())))

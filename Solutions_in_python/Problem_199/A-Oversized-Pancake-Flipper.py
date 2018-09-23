def get_flips():
    s, k = input().split()
    s = list(s)
    k = int(k)
    count = 0
    for i in range(len(s) - k + 1):
        if s[i] == '-':
            count += 1
            for j in range(i + 1, i + k):
                if s[j] == '-':
                    s[j] = '+'
                else:
                    s[j] = '-'
    for i in range(len(s) - k + 1, len(s)):
        if s[i] == '-':
            return 'IMPOSSIBLE'
    return count

for tc in range(1, int(input()) + 1):
    print(f'Case #{tc}:', get_flips())

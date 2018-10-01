for cases in range(1, int(input()) + 1):
    s = input()
    pattern, k = s.split()
    pattern = list(pattern)
    k = int(k)
    
    ans = 0
    for i in range(len(pattern) - k + 1):
        if(pattern[i] == '-'):
            ans += 1
            for j in range(i, i + k):
                pattern[j] = '+' if pattern[j] == '-' else '-'
    for i in range(len(pattern) - k, len(pattern)):
        if(pattern[i] == '-'):
            ans = 'IMPOSSIBLE'
            break
    print('Case #%d:' % (cases,), ans)

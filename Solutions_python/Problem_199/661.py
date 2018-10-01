def flip(s):
    res = ''
    for i in range(len(s)):
        if s[i] == '-':
            res = res + '+'
        else:
            res = res + '-'
    return res

def solve(test):
    s, k = input().strip().split()
    k = int(k)

    ans = 0
    for i in range(len(s)):
        if s[i] == '-':
            if i + k > len(s):
                ans = 'IMPOSSIBLE' 
            else:
                s = s[:i] + flip(s[i:i + k]) + s[i + k:]
                ans += 1
    print('Case #{}: '.format(test) + str(ans))

t = int(input())
for i in range(t):
    solve(i + 1)
        

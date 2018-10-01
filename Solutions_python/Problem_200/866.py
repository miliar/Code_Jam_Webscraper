def solve(n):
    s = [c for c in str(n)]
    l = len(s)
    i = 1
    while i < l:
        if int(s[l-i]) < int(s[l-i-1]):
            n -= (int(s[l-i])+1) * (10 ** (i-1))
            s = [c for c in str(n)]
            l = len(s)
            for j in range(l-i, l):
                s[j] = '9'
            n = int(''.join(s))
        else:
            i += 1
    return n

def inorder(n):
    s = str(n)
    for i in range(len(s)-1):
        if s[i] > s[i+1]:
            return False
    return True

def naive(n):
    for i in range(n):
        if inorder(n-i):
            return n-i

lines = [int(l) for l in open('input')]
N = lines[0]
for i in range(N):
    print('Case #%d: %d' % (i+1, solve(lines[i+1])))

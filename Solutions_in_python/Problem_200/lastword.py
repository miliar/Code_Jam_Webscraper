
def flip(x):
    c = ''
    for e in x:
        if e == '+':
            c+= '-'
        else:
            c+='+'
    return c

def pancake(s, k):
    if set(s) == {'+'}:
        return 0
    c = 0
    i = s.index('-')
    while i <= len(s) - k:
        temp = s[i:i+k]
        prev = s[:i]
        next = s[i+k:]
        s = prev + flip(temp) + next
        c += 1
        if set(s) == {'+'}:break
        i = s.index('-')
    if set(s) == {'+'}: return c
    return 'IMPOSSIBLE'


def tidy(n):
    if n < 10: return n
    n = list(str(n))
    l = n[-1]
    index = len(n) - 2
    for e in n[::-1][1:]:
        if e > l:
            n[index] = str(int(e) - 1)
            for i in range(index+1, len(n)):
                n[i] = '9'
        l = n[index]
        index -= 1
    return int(''.join(n))


n = int(raw_input().strip())
for i in range(n):
    s = int(raw_input().strip())
    print 'Case #%d: %s' % (i+1, tidy(s))

#!/usr/bin/python

S = dict()

def insert(H, s):
    if (s == ''):
        return
    if H.has_key(s[0]):
        H[s[0]][0] = H[s[0]][0] + 1
    else:
        H[s[0]] = [1, dict()]
    insert(H[s[0]][1], s[1:])
    return

def count(H, s, c = 1):
    if (s == ''):
        return c
    
    if s[0] == '(':
        pre = s[1:s.index(')')]
        suf = s[s.index(')')+1:]
        R = 0
        for i in range(len(pre)):
            if H.has_key(pre[i]):
                R = R + count(H[pre[i]][1], suf, H[pre[i]][0])
        return R
    else:
        if H.has_key(s[0]):
            return count(H[s[0]][1], s[1:], H[s[0]][0])
        else:
            return 0

if __name__ == '__main__':
    import sys
    inp = open(sys.argv[1], "r")
    (L, D, N) = inp.readline().split(' ')
    (L, D, N) = (int(L), int(D), int(N))
    for i in range(D):
        s = inp.readline().replace('\n', '')
        insert(S, s)
    for i in range(N):
        s = inp.readline().replace('\n', '')
        R = count(S, s)
        print 'Case #%s: %s' % ((i+1), R)

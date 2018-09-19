filled = []
tried = []
words = []
lists = []

def fits(w):
    if len(filled) == len(w):
        for i in range(len(w)):
            if (filled[i] == '.' and w[i] in tried) or (filled[i] != '.' and filled[i] != w[i]):
                return False
        return True
    else:
        return False

def fitsany(c):
    for w in words:
        if c in w and fits(w):
            return True

    return False

def fill(w, c):
    n = 0
    for i in range(len(w)):
        if w[i] == c:
            filled[i] = c
            n += 1

    return n

T = input()
for t in range(T):
    words = []
    lists = []
    N, M = [int(i) for i in raw_input().split()] 
    for i in range(N):
        words.append(raw_input())
    for i in range(M):
        lists.append(raw_input())

    res = []
    for list in lists:
        maxpunc = -1
        maxw = ''
        for w in words:
            punc = 0
            filled = ['.'] * len(w)
            tried = []
            fillnum = 0
            for c in list:
                if fillnum == len(w):
                    break

                if fitsany(c):
                    if c in w:
                        fillnum += fill(w, c)
                    else:
                        punc += 1

                tried.append(c)

            if punc > maxpunc:
                maxpunc = punc
                maxw = w

        res.append(maxw)

    print 'Case #%d: %s' % (t+1, ' '.join(res))


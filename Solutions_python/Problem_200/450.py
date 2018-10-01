def solve(d):
    idx = None
    for i in range(len(d) - 1):
        if d[i] > d[i+1]:
            idx = i
            break
    if idx is None:
        return ''.join(str(v) for v in d)

    p = None
    for i in range(idx, 0, -1):
        if d[i] > d[i-1]:
            p = i
            break
    if p is None:
        if d[0] > 1:
            d[0] -= 1
            for i in range(1,len(d)):
                d[i] = 9
            return ''.join(str(v) for v in d)
        return (len(d) - 1)*'9'
    for i in range(p+1, len(d)):
        d[i] = 9
    d[p] -= 1
    return ''.join(str(v) for v in d)

f = open('in.txt')

cases = int(f.readline())
for i in range(1, cases + 1):
    t = f.readline()
    d = [int(v) for v in t[:-1]]
    print('Case #%s: '%i + solve(d))

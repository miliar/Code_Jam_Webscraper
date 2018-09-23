T = int(input().strip())

def maketidy(numstr):
    ns = list(numstr)
    for i in range(len(numstr)-1, 0, -1):
        if int(ns[i]) >= int(ns[i-1]):
            continue
        ns[i] = '9'
        j = i-1
        while j >= 0:
            if ns[j] != '0':
                ns[j] = str(int(ns[j]) - 1)
                for k in range(j+1, len(ns)):
                    ns[k] = '9'
                break
            ns[j] = '9'
            j = j - 1
    rv = ''.join(ns)
    if rv[0] == '0':
        rv = rv[1:]
    return rv

for t in range(1, T+1):
    N = input().strip()
    mt = maketidy(N)
    print('Case #%d: %s' % (t, mt))
    

def wp_except(rr, n, j):
    w = 0
    pn = 0
    jj = 0
    for r in rr:
        if jj!=j:
            if r!='.':
                pn += 1
            if r=='1':
                w += 1
        jj += 1
    return float(w)/pn


def solve(t):
    print "Case #%d:" % t
    n = int(raw_input())
    res = {}
    for i in range(n):
        res[i] = raw_input().strip()

    wp = {}
    for i in range(n):
        w = 0
        pn = 0
        for r in res[i]:
            if r!='.':
                pn += 1
            if r=='1':
                w += 1
        wp[i] = float(w)/pn

    op = {}
    for i in range(n):
        j = 0
        p = 0
        pn = 0
        for r in res[i]:
            if r!='.':
                p += wp_except(res[j], n, i)
                pn += 1
            j += 1

        op[i] = float(p)/pn

    oop = {}
    for i in range(n):
        j = 0
        p = 0
        pn = 0
        for r in res[i]:
            if r!='.':
                p += op[j]
                pn += 1
            j += 1

        oop[i] = float(p)/pn

    for i in range(n):
        print 0.25*wp[i] + 0.5*op[i] + 0.25*oop[i]
            

def main():
    t = int(raw_input())
    for i in range(t):
        solve(i+1)

if __name__ == '__main__':
    main()

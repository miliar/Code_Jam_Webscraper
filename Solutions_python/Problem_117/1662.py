n = int(raw_input())
for i in range(n):
    n, m = raw_input().split()
    n, m = int(n),int(m)
    lawn = []
    for j in range(n):
        lawn += [raw_input().split()]
    
    ans = 'YES'
    for j in range(n):
        for k in range(m):
            cheight = lawn[j][k]
            for l in range(n):
                if lawn[l][k] > cheight:
                    ok = False
                    break
            else:
                ok = True

            if not ok:
                for l in range(m):
                    if lawn[j][l] > cheight:
                        ok = False
                        break
                else:
                    ok = True

            if not ok:
                ans = 'NO'
                break
        else:
            continue
        break
    print 'Case #%d: %s' % (i+1, ans)               

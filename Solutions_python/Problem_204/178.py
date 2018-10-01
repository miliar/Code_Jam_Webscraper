from codejam import CodeJam

from math import ceil

def testcase(f):
    (N, P) = [int(i) for i in f.readline().split()]
    R = [int(i) for i in f.readline().split()]
    Q = []
    for _ in range(N):
        Q.append(sorted(int(i) for i in f.readline().split()))

    #QQ = []
    #for (i, ingred) in enumerate(Q):
    #    for package in ingred:
    #        QQ.append((package, i))
    #QQ.sort()
    #QQ = [i[1] for i in QQ]

    kits = 0
    try:
        while True:
            mn = (Q[0][0] * 10 / (11 * R[0]), 0)
            for n in range(1, N):
                mn = min(mn, (Q[n][0] * 10 / (11 * R[n]), n))
            (mn, ingnum) = mn
            package = Q[ingnum].pop(0)
            mn = int(ceil(mn))
            mx = int(package * 10 / (9 * R[ingnum]))
            if mn > mx:
                continue
            for i in range(N):
                if i != ingnum:
                    mn = int(ceil(Q[i][0] * 10 / (11 * R[i])))
                    if mn > mx:
                        break
            else:
                for i in range(N):
                    if i != ingnum:
                        Q[i].pop(0)
                kits += 1
    except IndexError:
        pass
    return kits




    
            


cj = CodeJam(testcase)

# After importing cj into an interactive terminal, I test the code by
# running:
# >>> cj.processtext("""examples""")
#
# Then after downloading the problem set, I solve it with:
# >>> cj.processfile('filename')

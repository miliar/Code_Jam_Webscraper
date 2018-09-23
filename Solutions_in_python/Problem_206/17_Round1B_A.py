from rope.base.pyobjectsdef import _AssignVisitor

for T in range(int(input())):
    D, N = [int(x) for x in input().strip().split(' ')]

    K = []
    S = []
    for n in range(N):
        k,s  = [int(x) for x in input().strip().split(' ')]
        K.append(k)
        S.append(s)

    S = [x for (y, x) in sorted(zip(K, S))]
    K = sorted(K)

    S = S[::-1]
    K = K[::-1]

    prev = 0
    for i in range(len(S)):
        fat = float((D-K[i])/S[i])

        if fat > prev or prev == 0:
            prev = fat



    print("Case #%d: %.6f" % (T+1, D/prev))
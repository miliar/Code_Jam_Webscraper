T = int(input())

for t in range(1, T+1):
    n, R, O, Y, G, B, V = map(int, input().split())

    aa, bb, cc = sorted([(R, "R"), (Y, "Y"), (B, "B")])
    
    a, b, c = aa[0], bb[0], cc[0]
    A, B, C = aa[1], bb[1], cc[1]

    print("Case #%d: " % (t, ), end="")

    if a+b>=c:
        k = a+b-c
        print((C+A+B)*k + (C+A)*(a-k) + (C+B)*(c-a))
    else:
        print("IMPOSSIBLE")

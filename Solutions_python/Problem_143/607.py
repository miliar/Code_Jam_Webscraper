with open('B-small-attempt0.in') as file:
    cases = int(file.readline())
    output = open('output.txt','w')
    for c in range(1, cases + 1):
        raw = file.readline().split()
        A = int(raw[0])
        B = int(raw[1])
        K = int(raw[2])
        ans = 0
        for i in range(A):
            for j in range(B):
                if (i & j) < K:
                    ans += 1
        print (ans)
        output.write('Case #%d: %d\n'% (c, ans))

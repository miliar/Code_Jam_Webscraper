import math
t = int(input())
for caseN in range(1, t+1):
    n, k = [ int(x) for x in input().split() ]
    b = int(math.log2(k))
    a = k - 2**b
    if n < 2*k - a: print("Case #%d: 0 0" % caseN)
    else:
        plus = int((n - 2*k + a) / (2**b)) + 1
        if plus % 2 == 0: print("Case #%d: %d %d" % (caseN, plus//2, plus//2))
        else: print("Case #%d: %d %d" % (caseN, plus//2 + 1, plus//2))

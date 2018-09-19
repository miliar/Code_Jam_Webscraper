import sys

sys.setrecursionlimit(1000000)

f = open(sys.argv[1]) if len(sys.argv)>1 else sys.stdin

total = int(f.readline().strip())

for i in range(total):
    sys.stdout.write("Case #%d: " % int(i+1))
    A, B, K = [int(j.strip()) for j in f.readline().split()]
    r = 0
    for i in range(A):
        for j in range(B):
            if i & j < K:
                r += 1
    print(r)

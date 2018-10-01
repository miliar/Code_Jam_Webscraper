import sys

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    line = input().split()
    d = float(line[0])
    n  = int(line[1])
    hs = []
    t = 0
    for j  in range(n):
        line = input().split()
        t=max(t,(d-float(line[0]))/float(line[1]))
    print("Case #{}: {}".format(i, d/t))
    # print(i, file=sys.stderr) #DEBUG

def mymin(a, b):
    (x, y) = a
    (c, d) = b
    if x > c or (x == c and y > d):
        return b
    else:
        return a

bathdata = {}
def bath(n, k):
    if (n, k) in bathdata:
        return bathdata[(n, k)]
    if k == 1:
        return (n//2, (n-1)//2)
    elif k == 2:
        return bath(n//2, 1)
    else:
        bathdata[(n, k)] = mymin(bath(n//2, k//2), bath((n-1)//2, (k-1)//2))
    return bathdata[(n, k)]

import sys
T = sys.stdin.readline()
for i, line in enumerate(sys.stdin):
    n, k = line.split(" ")
    n = int(n)
    k = int(k)
    n1, n2 = bath(n, k)
    print("CASE #{}: {} {}".format(i+1, n1, n2))
    if T == i+1:
        break

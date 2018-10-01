import sys

t = int(sys.stdin.readline())
for c in range(1, t + 1):
    n = int(sys.stdin.readline())
    a = sys.stdin.readline().strip().split()
    a.sort()
    b = sys.stdin.readline().strip().split()
    b.sort()
    i = 0
    j = 0
    z = 0
    while i < len(a):
        while j < len(b) and b[j] < a[i]:
            j += 1
        if j < len(b):
            j += 1
        else:
            z += 1
        i += 1
    y = 0
    i = 0
    j = 0
    while i < len(a):
        if a[i] > b[j]:
            y += 1
            i += 1
            j += 1
        else:
            i += 1

    print 'Case #%d: %d %d' %(c, y, z)


import sys

def find_row(arr, x):
    for i, row in enumerate(arr):
        if x in row:
            return i
    return -1

T = int(sys.stdin.readline())
for i in range(T):
    r1 = int(sys.stdin.readline()) - 1
    arr1 = [map(int, sys.stdin.readline().split()) for j in range(4)]
    r2 = int(sys.stdin.readline()) - 1
    arr2 = [map(int, sys.stdin.readline().split()) for j in range(4)]
    res = []
    for j in range(1, 17):
        if find_row(arr1, j) == r1 and find_row(arr2, j) == r2:
            res.append(j)
    if len(res) == 1:
        print 'Case #%d: %d' % (i+1, res[0])
    elif len(res) == 0:
        print 'Case #%d: Volunteer cheated!' % (i+1)
    else:
        print 'Case #%d: Bad magician!' % (i+1)


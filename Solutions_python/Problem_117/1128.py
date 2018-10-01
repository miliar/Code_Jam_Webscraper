# Python version 2.7
import sys

size = 4

def oneCase():
    [n,m] = map(int, sys.stdin.readline().split(' '))
    lawn = []
    for i in range(n):
        lawn.append(map(int, sys.stdin.readline().split(' ')))
    rows = map(lambda i: max(lawn[i]), range(n))
    columns = map(lambda i: max(map(lambda x: x[i], lawn)), range(m))
    for i in range(n):
        for j in range(m):
            if lawn[i][j] != min(rows[i], columns[j]): return False
    return True
    

cases = int(sys.stdin.readline())
for i in range(cases):
    print "Case #" + str(i+1) + ": " + ("YES" if oneCase() else "NO") 
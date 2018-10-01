import sys

def ri():
    return map(int, sys.stdin.readline().split())


T = int(input())


for i in range(T):
    count = 0
    face, k = sys.stdin.readline().split()
    face = list(face)
    k = int(k)
    for j in range(len(face)-k+1):
        if face[j] == '-':
            count += 1
            for jj in range(k):
                if face[j+jj] == '-':
                    face[j+jj] = '+'
                else:
                    face[j+jj] = '-'
    if '-' in face:
        print("Case #%d: IMPOSSIBLE"%(i+1))
    else:
        print("Case #%d: %d"%(i+1, count))

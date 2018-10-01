import math
import heapq
import copy
import itertools

def perm(P, k, string):
    res = []
    offset = 0
    for i in range(int(len(string)/k)):
        for j in range(k):
            res.append(string[offset + P[j]])
        offset += k
    return res

def RLE(string):
    last = '!'
    res = 0
    for i in range(len(string)):
        if string[i] != last:
            last = string[i]
            res+= 1
    return res


            
    

def main():
    ifile = open('b.in', 'r')
    ofile = open('b.out', 'w')

    
    T = int(ifile.readline().strip())
    for case in range(1, T+1):
        N = int(ifile.readline().strip())
        A = [int(x) for x in ifile.readline().split()]
        
        m = max(A)
        pos = 0
        for i in range(N):
            if A[i] == m:
                pos = i

        move = [0 for i in range(N)]
        umove = [0 for i in range(N)]
        for a in range(N):
            for b in range(a+1, N):
                if a == b:
                    continue
                if A[a] > A[b]:
                    i, j = a, b
                else:
                    i, j, = b, a
                if i == pos:
                    move[j] += 1
                elif i < pos and j > pos:
                    move[j] += 1
                elif i > pos and j < pos:
                    move[j] += 1
                elif i < pos and j < pos:
                    if i < j:
                        umove[j] += 1
                    else:
                        move[j] += 1
                elif i > pos and j > pos:
                    if j > i:
                        move[j] += 1
                    else:
                        umove[j] += 1
        res = 0
##        print(move, umove)
        for i in range(N):
            res += min(move[i], umove[i])
            
        print(res)
        ofile.write('Case #%d: %d\n' %(case, res))

        

if __name__ == "__main__":
    main()

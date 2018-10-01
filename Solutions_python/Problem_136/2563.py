import sys
import math

S = 2

def ReadIn():
    cases = int(input())
    for c in range(1, cases + 1):
        C, F, X = [float(x) for x in input().split()]
        yield c, C, F, X
        
def Solve(C, F, X):
    upper = (X * F - C * S - C * F) / (C * F)
    k = max(0, int(math.ceil(upper)))
    result = 0
    for i in range(k):
        result += C / (S + i * F)
    result += X / (S + k * F)
    return result

if __name__ == '__main__':
    for case, C, F, X in ReadIn():
        print('Case #%d: %.6f' % (case, Solve(C, F, X)))
import math

def sqr(i):
    return i*i

N, M, K = 0, 0, 0

def factor(x):
    global N
    rest = x
    result = []
    for i in reversed(range(2, M + 1)):
        while (rest % i) == 0:
            rest = rest // i
            result.append(i)
        if rest == 1:
            break
        
    return result

def mergeRes(r, append):
    remainder = r[:]
    result = r[:]
    for i in append:
        if i in remainder:
            remainder.remove(i)
        else:
            result.append(i)
    
    return result
        
        
def solveCase(c):
    global N, M, K

    result = [] # [0 for i in range(1, K)]
    
    for x in c:
        append = factor(x)
        result = mergeRes(result, append)
        print('x,a,c', x, append, result)
        
    l = len(result)
    if l < N:
        result.extend([2 for i in range(0, N - l)])
        
    string = ''
    for i in result:
        string = string + str(i)
    print(string)
              
    return string



def solve(sourceFile, resultFile):
    global N, M, K

    s = open(sourceFile)
    res = open(resultFile, 'w')

    t = int(s.readline())
    
    r, N, M, K = [int(i) for i in s.readline().split()]
    print('n,k,m', N, K, M)

    header = 'Case #1: \n'
    res.write(header)
    for n in range(1, r + 1):
        string = s.readline()
        case = [int(i) for i in string.split()]
        res.write(solveCase(case) + '\n')
        
    return
        
def main():
    source = 'C-small-1-attempt1.in'
    result = source + '.result.txt'
    solve(source, result)
    return

if __name__ == '__main__':
    main()

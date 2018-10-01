def sqr(i):
    return i*i

def solveCase1(case):
    print(case)
    r = case[0]
    t = case[1]
    result = 0
    currentRadius = r
    
    while t>0:
        square = sqr(currentRadius + 1) - sqr(currentRadius)
        if square <= t:
            result = result + 1
            t = t - square
        else:
            break
        currentRadius = currentRadius + 2
        
    return str(result)
    

def solve(sourceFile, resultFile):
    s = open(sourceFile)
    r = open(resultFile, 'w')

    count = int(s.readline())
    for n in range(1, count + 1):
        string = s.readline()
        case = [int(i) for i in string.split()]

        header = 'Case #' + str(n) + ': '
        r.write(header + solveCase1(case) + '\n')
    return
        
def main():
    source = 'A-small-attempt2.in'
    result = source + '.result.txt'
    solve(source, result)
    return

if __name__ == '__main__':
    main()

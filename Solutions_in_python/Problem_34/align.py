import sys

ord_a = ord('a')

def code(char):
    return 2**(ord(char) - ord_a)

def testpattern(testcase):
    result = []
    tmp = -1
    for c in testcase:
        if c == '(':
            tmp = 0
        elif c == ')':
            result.append(tmp)
            tmp = -1
        else:
            if tmp == -1:
                result.append(code(c))
            else:
                tmp |= code(c)
    return result


def test(testcase, words):
    pattern = testpattern(testcase)
    
    result = 0
    for word in words:
        for i in range(len(word)):
            if pattern[i] & code(word[i]) == 0:
                break
        else:
            result += 1
    
    return result


def main():
    input = open(sys.argv[1])
    L, D, N = (int(t) for t in input.readline().split())
    
    words = [input.readline().strip() for i in range(D)]
    
    for i in range(1, N+1):
        testcase = input.readline().strip()
        print 'Case #%d:' % i, test(testcase, words)
    

if __name__ == '__main__':
    main()
    
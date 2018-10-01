


def palindromeCheck(num):
    num = str(num)
    i = 0
    j = len(str(num))-1
    while True:
        if num[i] == num[j]:
            i = i+1
            j = j-1
            if i>j or i==j:
                return True 
        else:
            return False


def computePalindrome(limit=10**14):
    pval = []
    sqr_pval = []
    for i in xrange(1,10**10):
        if palindromeCheck(i):
            if i*i > limit:
                break
            if palindromeCheck(i*i):
                pval.append(i*i)
    print pval
    return pval


def main():
    pval = computePalindrome(limit=10**14)
    f = open('C-large-1.in', 'r')
    r = open('C-large-1.in-result', 'w')

    while True:
        line = f.readline()
        if not line:
            break
        caseNum = int(line)
        for i in range(caseNum):
            start, end = f.readline().rstrip().split(' ')
            result = [ x for x in pval if x >= int(start) and x<=int(end)]
            result_line = 'Case #' + str(i + 1) + ': ' + str(len(result))
            r.write(result_line + '\n')
            print result_line

    f.close()
    r.close()   


if __name__ == '__main__':
    main()










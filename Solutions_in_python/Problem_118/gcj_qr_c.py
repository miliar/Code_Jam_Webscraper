from bisect import bisect_left, bisect_right
def ispalindrome(n):
    c = 0
    while True:
        c = c * 10 + n % 10
        if c == 0:
            return False
        if c == n:
            return True
        if c > n:
            return False
        n = n /10
        if c == n:
            return True
        if c > n:
            return False
        
def reverse(n):
    c = 0
    while n:
        c = c * 10 + n % 10
        n = n / 10
    return c

def palindromes(n):
    c = 1
    s = 1
    for i in xrange(1, n + 1):
        t = 10 ** (i - 1)
        for j in xrange(t, 10 ** i):
            yield j * t + reverse(j / 10)
        t = 10 * t
        for j in xrange(10 ** (i - 1), 10 ** i):
            yield j * t + reverse(j)
        
def getfairsquares(n):
    l = []
    for i in palindromes(n):
        s = i * i
        if ispalindrome(s):
            l.append(s)
    return l

n = 4

def getnumbers(l, b, e):
    i = bisect_left(l, b)
    j = bisect_right(l, e)
    #print l, i, j
    return j - i

file_prefix = 'C-large-1'
input_file = file_prefix + '.in'
output_file = file_prefix + '.out'

def main():
    numbers = getfairsquares(n)
    ifs = open(input_file, 'rb')
    ofs = open(output_file, 'wb')
    itr = iter(ifs)
    t = int(itr.next().strip())
    for i in range(t):
        interval = map(int, itr.next().strip().split())
        b, e = interval[0], interval[1]
        ofs.write('Case #%d: %d\n' % (i + 1,
                                      getnumbers(numbers, b, e)))

if __name__ == '__main__':
    main()
    

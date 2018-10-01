import os, math

def column(mat, n):
    return [row[n] for row in mat]


def columns(mat):
    return (column(mat, n) for n in xrange(len(mat[0]))) if mat else ()


def rows(mat):
    return (list(m) for m in mat)


def mkmat(val, m, n):
    return [x[:] for x in [[val] * n] * m]


def check(mat):
    pass

def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

def palindrome_gen(A, B):
    lower = int(math.ceil(math.sqrt(A)))
    upper = int(math.floor(math.sqrt(B)))

    yield 1
    yield 2
    yield 3
    while True:
        for n in ('1','2'):
            yield n + n


def palindromes(l, inside=False):
    for i in ('0','1','2') if inside else ('1','2'):
        if l == 1:
            yield i
        elif l == 2:
            yield i + i
        else:
            for j in palindromes(l-2, True):
                yield ''.join([i,j,i])



def count_palindromes(A, B):
    length =  len(str(int(math.ceil(math.sqrt(A)))))
    count = 1 if A <= 9 <= B else 0 # the one special case...
    while True:
        for p in palindromes(length):
            square = int(p)**2
            if square < A:
                continue
            if square > B:
                return count
            if is_palindrome(square):
                count += 1
        length += 1


def main():
    inpath = 'C-large-1.in'
    outpath = os.path.splitext(inpath)[0] + '.out'
    with open(inpath, 'r') as infile, open(outpath, 'w') as outfile:
        T = int(infile.readline())
        for t in xrange(T):
            A, B = map(int, infile.readline().split())
            ans = count_palindromes(A, B)
            #print '#%d: %d %d -> %d' % (t+1,A,B,ans)
            outfile.write('Case #%d: %d\n' % (t + 1, ans))


if __name__ == '__main__':
    main()

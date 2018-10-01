import bisect
def is_palindrome(x):
    digits = []
    while x > 0:
        digits.append(x % 10)
        x /= 10
    i = 0
    while i <= (len(digits) - i - 1):
        if digits[i] != digits[len(digits) -i - 1]:
            return False
        i += 1
    return True

def palindromes(n):
    for i in xrange(1, n + 1):
        if is_palindrome(i):
            yield i

def fairs(n):
    for x in palindromes(n):
        sq = x ** 2
        if sq > n:
            return
        if is_palindrome(x ** 2):
            yield sq
        

FAIRS = list(fairs(10 ** 14))
def count_fairs(a):
    return bisect.bisect_left(FAIRS, a)
    
def solve(in_file_name, out_file_name):
    in_file = open(in_file_name)
    out_file = open(out_file_name, "wt")
    ncases = int(in_file.readline())
    for ncase in xrange(1, ncases + 1):
        a, b = map(int, in_file.readline().split())
        out_file.write("Case #%d: %d\n" % (ncase, count_fairs(b + 1) - count_fairs(a)))
    out_file.close()

# Code Jam 2017 Qualification round
# MichelJ
# Problem B: Tidy Numbers

def stidy(s):
    for i in xrange(1, len(s)):
        if s[i] < s[i - 1]:
            return False
    return True

def tidy(x):
    return stidy(map(int, str(x)))

def solve_brute(n):
    for x in xrange(n, 0, -1):
        if tidy(x):
            return str(x)

def solve(n):
    s = map(int, str(n))
    l = len(s)
    sol = s[:]
    for i in xrange(l - 2, -1, -1):
        nd = s[i]
        if nd > sol[i + 1]:
            sol[i] = nd - 1
            for j in xrange(i + 1, l):
                sol[j] = 9
    while sol[0] == 0:
        sol.pop(0)
    return "".join(map(str, sol))

def main():
    for t in xrange(input()):
        n = input()
        res = solve(n)
        print "Case #%d:"%(t + 1), res
        
main()

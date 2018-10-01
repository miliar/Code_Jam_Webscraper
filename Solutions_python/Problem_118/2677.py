import sys
import io
from math import sqrt

def isPalindrome(n):
    s = str(n)
    if len(s) % 2 == 1:
        s = s[:len(s) / 2] + s[len(s) / 2 + 1:]
    if len(s) == 0:
        return True
#    print("isPalindrome string: " + s + " first half: " + s[:len(s) / 2])
    for i in range(len(s) / 2):
        if s[i] != s[i + len(s) / 2]:
            return False
    return True

f = io.open("C-small-attempt0.in")
o = io.open("Output", "w")

testcases = int(str(f.readline()).strip())
for case in range(testcases):
    mini, maxim = [int(x) for x in str(f.readline()).strip().split()]
    minirt = int(sqrt(mini))
    maxrt = int(sqrt(maxim))
    if minirt * minirt < mini:
        minirt += 1
    if maxrt * maxrt > maxim:
        maxrt -= 1
#    print(mini, maxim, range(minirt, maxrt + 1)[0], range(minirt, maxrt + 1)[-1])
    palindromes = 0
    for i in range(minirt, maxrt + 1):
        if isPalindrome(i) and isPalindrome(i * i):
            palindromes += 1
    #print("Case #" + str(case) + ": " + str(palindromes))
    o.write(unicode("Case #" + str(case + 1) + ": " + str(palindromes) + "\n"))
o.close()

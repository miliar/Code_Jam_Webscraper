from math import sqrt, floor, ceil

def is_palindrome(n):
    s = str(n)
    if s == '':
        return True
    else:
        if (ord(s[0]) - ord(s[len(s)-1])) == 0:
            return is_palindrome(s[1:len(s)-1])
        else:
            return False

name = "B-small-attempt0"
f = open(name + ".in", "r")
line_num = 0
cases = {}

for line in f:
    line_num += 1
    if line_num > 1:
        cases[line_num-1] = [int(i) for i in line.strip().split(" ")]

f.close()

g = open(name + ".out", "w")

for i in range(1, line_num):
    num_fair_square = 0
    for j in range(int(ceil(sqrt(cases[i][0]))), int(floor(sqrt(cases[i][1]))) + 1):
        if is_palindrome(j) and is_palindrome(pow(j, 2)):
            num_fair_square += 1
    g.write("Case #" + str(i) + ": " + str(num_fair_square) + "\n")

g.close()
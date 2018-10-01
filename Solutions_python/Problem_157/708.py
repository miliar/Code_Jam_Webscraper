#!/usr/bin/env python
import sys
table = {
          (1,1):1, (1,105):105, (1,106):106, (1,107):107,
          (105,1):105, (105,105):-1, (105,106):107, (105,107):-106,
          (106,1):106, (106,105):-107, (106,106):-1, (106,107):105,
          (107,1):107, (107,105):106, (107,106):-105, (107,107):-1
        }
def multi(a, b):
    sign = 1
    if a*b < 0:
        sign = -1
    return sign * table[(abs(a), abs(b))]

def solve(line):
    l, x = (int(t) for t in line.split())
    p = raw_input()

    if l * x <3:
        return "NO"

    s = p * x

    part2s = [1] * (l*x)
    part2 = 1
    for j in xrange(l*x - 1, 0, -1):
        part2 = multi(ord(s[j]), part2)
        part2s[j] = part2

    part0 = 1
    for i in xrange(0, l*x - 2):
        part0 = multi(part0, ord(s[i]))
        if part0 == ord("i") and part2s[i+1] == ord("i"):
            part1 = 1
            for j in xrange(i+1, l*x - 1):
                part1 = multi(part1, ord(s[j]))
                if part1 == ord("j") and part2s[j+1] == ord("k"):
                    # print part2s[j+1]
                    # print part2s[i+1]
                    # print s[:i+1], s[i+1:j+1], s[j+1:]
                    return "YES"

    return "NO"

case_num = input()
for case in range(1, case_num + 1):
    sys.stderr.write(str(case))
    line = raw_input()
    print("Case #%i: %s" % (case, solve(line)))
    sys.stderr.write("\n")


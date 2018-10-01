__author__ = 'Ruben'
import util
import math

def is_palindrome(s):
    #print s
    if len(s) % 2 == 1:
        mid = int(math.floor(len(s) / 2))
        first_half = s[: mid]
        second_half = s[mid + 1:]
        if first_half == second_half[::-1]:
            return True
    else:
        first_half = s[: len(s) / 2]
        second_half = s[len(s) / 2:]
        if first_half == second_half[::-1]:
            return True

    return False

#print is_palindrome("1")
#print is_palindrome("22")
#print is_palindrome("676")
#exit()

file = open("C-small-attempt0.in")
#file = open("qual_03.txt")

cases = int(file.readline().strip())

for c in xrange(cases):
    tmp = file.readline().strip().split(" ")
    s = int(tmp[0])
    e = int(tmp[1])

    c += 1

    found = 0

    for i in xrange(s, e+1):
        sq = util.int_square(i)
        if is_palindrome(str(i)) and sq != -1 and is_palindrome(str(sq)):
            #print i
            found += 1

    print "Case #" + str(c) + ": " + str(found)

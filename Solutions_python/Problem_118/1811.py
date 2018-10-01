"""
from math import sqrt

results = [1,4,9]

for i in results:
    print i

for d in xrange(2, 16):
    if d % 2 == 0:
        for i in xrange(10**(d/2-1), 10**(d/2)):
            str_i = str(i)
            palindrome = int("{}{}".format(str_i,str_i[::-1]))
            root = int(sqrt(palindrome))
            if root ** 2 == palindrome:
                root_str = str(root)
                if root_str == root_str[::-1]:
                    print palindrome
                    results.append(palindrome)
    else:
        for i in xrange(10**(d/2), 10**(d/2+1)):
            palindrome = int("{}{}".format(str(i), str(i/10)[::-1]))
            root = int(sqrt(palindrome))
            if root ** 2 == palindrome:
                root_str = str(root)
                if root_str == root_str[::-1]:
                    print palindrome
                    results.append(palindrome)
"""
import sys

table = [
    1,
    4,
    9,
    121,
    484,
    10201,
    12321,
    14641,
    40804,
    44944,
    1002001,
    1234321,
    4008004,
    100020001,
    102030201,
    104060401,
    121242121,
    123454321,
    125686521,
    400080004,
    404090404,
    10000200001,
    10221412201,
    12102420121,
    12345654321,
    40000800004,
    1000002000001,
    1002003002001,
    1004006004001,
    1020304030201,
    1022325232201,
    1024348434201,
    1210024200121,
    1212225222121,
    1214428244121,
    1232346432321,
    1234567654321,
    4000008000004,
    4004009004004,
    100000020000001,
    100220141022001,
    102012040210201,
    102234363432201,
    121000242000121,
    121242363242121,
    123212464212321,
    123456787654321,
    400000080000004,
]

lines = sys.stdin.readlines()
T = int(lines[0])

for i in range(1,T+1):
    A, B = map(int, lines[i].split(" "))
    count = 0
    for t in table:
        if t >= A and t <= B:
            count += 1
    print("Case #{}: {}".format(i,count))

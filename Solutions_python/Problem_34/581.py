import sys
import re

nums = sys.stdin.readline()
[lword, ldict, lpattern] = nums.split(' ')

dic = []
lines = sys.stdin.readlines()
for i in range(0,int(ldict)):
    dic.append(lines[i][0:-1])
"""
print "Dictionary:", len(dic)
for i in dic:
    print i
print "--------------------------------"
"""
patterns = []
for i in range(int(ldict), len(lines)):
    patterns.append(lines[i][0:-1])

bloodyregexps = []
for pattern in patterns:
    if pattern.find('(') != -1:
        pattern = pattern.replace('(', '[')
        pattern = pattern.replace(')', ']')
    bloodyregexps.append(re.compile(pattern))

case = 1
for bloodyregexp in bloodyregexps:
    count = 0
    #print "Pattern: ", pattern
    for i in dic:
        if bloodyregexp.match(i):
            #print bloodyregexp.findall(i)
            count = count + 1
    print 'Case #%d: %d' % (case, count)
    case = case + 1

import sys
import re

line = sys.stdin.readline().strip()
values = line.split()

words = ''
for wordNum in range(int(values[1])):
    word = sys.stdin.readline().strip()
    words = words + '|' + word
words += '|'


for inputNum in range(int(values[2])):
    input = sys.stdin.readline().strip()
    input = input.replace('(', '[')
    input = input.replace(')', ']')
    pattern = re.compile(input)
    matches = pattern.findall(words)
    print 'Case #%d: %d' % (inputNum + 1, len(matches))
    
import re

input_file = open('input.txt','r')
output = open('output.txt','w')

L,D,N = input_file.readline().strip().split()

words = []
cases = []
for x in range(int(D)):
    words.append( input_file.readline().strip() )
for x in range(int(N)):
    s = input_file.readline().strip()
    s = '^' + s + '$'
    s = s.replace('(','[').replace(')',']')
    cases.append(s)

input_file.close()

count = 0
for x in range(len(cases)):
    count += 1
    s = 'Case #%s: ' % count
    matches = 0
    for y in range(len(words)):
        if re.match(cases[x], words[y]): matches += 1
    s += '%s\n' % matches
    print s
    output.write(s)

output.close()

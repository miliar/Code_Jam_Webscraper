import re

input_data = open("A-small-attempt0.in", "rU")
output_data = open("A-small-attempt0.out", "w")

def matches(pattern):
    pattern = pattern.replace('(', '[')
    pattern = pattern.replace(')', ']')
    return len(re.findall(pattern, ' '.join(dictionary)))

l, d, n = input_data.readline().split(' ')
dictionary = []

for i in xrange(int(d)):
    dictionary.append(input_data.readline().strip('\n'))

for i in xrange(int(n)):
    output_data.write("Case #%d: %d" % (i + 1, matches(input_data.readline().strip('\n'))))

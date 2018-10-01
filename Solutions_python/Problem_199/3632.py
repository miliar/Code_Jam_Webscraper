def flip(array):
    substringarray = []
    for stri in array:
        if stri == '-':
            substringarray.append('+')
        else:
            substringarray.append('-')
    return substringarray
with open('small.in', 'r') as f:
    lines = f.readlines()

row = 0
for line in lines[1:]:
    pancakes = []
    row += 1
    substringarray = []
    string = line.split()
    counter = 0
    for ch in string[0]:
        pancakes.append(ch)
    k = int(string[1])
    length = len(pancakes)
    for i in xrange(0, length):
        if length-i < k:
            if '-' in pancakes[i:]:
                counter = 'IMPOSSIBLE'
                break
        elif pancakes[i] == '-':
            substringarray = flip(pancakes[i:i+k])
            counter = counter + 1
            for j in xrange(0, len(substringarray)):
               pancakes[i+j] = substringarray[j]
        elif pancakes[i] == '+':
            continue

    print 'Case #%r: %s' % (row, counter)

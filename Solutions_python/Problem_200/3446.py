import sys

def last_tidy_number(digits):
    changed = True
    while changed:
        changed = False
        for i in range(len(digits) - 1, 0, -1):
            if digits[i - 1] > digits[i]:
                changed = True
                digits[i - 1] -= 1
                for j in range(i, len(digits), 1):
                    digits[j] = 9
                
    return ''.join([str(d) for d in digits]).lstrip('0')

with open(sys.argv[1]) as infile:
    infile.readline()
    for index, line in enumerate(infile, 1):
        print 'Case #%d: %s' % (index, last_tidy_number([int (x) for x in line[:-1]]))


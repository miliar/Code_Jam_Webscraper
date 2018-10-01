import sys
from sets import Set

def count_all_pairs(a, b):
    pairs = 0
    for i in xrange(int(a), int(b)):
        pairs += count_valid_pairs(str(i), int(b))
    return pairs

def count_valid_pairs(num, maximum):
    if len(num) <= 1:
        return 0
    numbers = Set()
    cut = 1
    while cut < len(num):
        subset = num[-cut:]
        newnum = subset + num[:len(num) - cut]
        if newnum[0] != '0' and int(newnum) > int(num) and int(newnum) <= maximum:
            numbers.add(newnum)
        cut += 1
    return len(numbers)

if __name__ == '__main__':
    f = open(sys.argv[1], 'r')
    out = open('out.txt', 'w')
    cases = int(f.readline())
    for i in xrange(1, cases + 1):
        a, b = f.readline().replace('\n', '').split(' ')
        case = 'Case #{0}: {1}\n'.format(i, count_all_pairs(a, b))
        #print case,
        out.write(case)
    f.close()
    out.close()

import sys

# skip num test cases
sys.stdin.readline()

for case, line in enumerate(sys.stdin, 1):
    s_max, digits = line.split()
    s_max = int(s_max)
    amounts = [(i, int(v)) for i, v in enumerate(digits) if v != '0']

    count = 0
    min_required = 0
    for shyness_level, amount in amounts:
        if count < shyness_level:
            min_required += shyness_level - count
            count += shyness_level - count
        count += amount

    print 'Case #%d: %d' % (case, min_required)

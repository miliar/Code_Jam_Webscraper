import sys

def test_line(line):
    if 'X' not in line and '.' not in line:
        return 'O'
    if 'O' not in line and '.' not in line:
        return 'X'
    if '.' in line:
        return '.'
    return 'T'

def test(lines, case):
    not_completed = False
    test_lines = lines
    for col in range(0,4):
        test_lines.append(lines[0][col] + lines[1][col] + lines[2][col] + lines[3][col])
    test_lines.append(lines[0][0] + lines[1][1] + lines[2][2] + lines[3][3])
    test_lines.append(lines[3][0] + lines[2][1] + lines[1][2] + lines[0][3])
    for line in test_lines:
        ret = test_line(line)
        if ret in 'XO':
            return 'Case #%i: %s won' % (case, ret)
        if ret == '.':
            not_completed = True
    if not_completed:
        return 'Case #%i: Game has not completed' % case
    return 'Case #%i: Draw' % case

with open(sys.argv[1]) as f:
    N = int(f.readline())
    for case in range(1,N+1):
        lines = []
        for line in range(1,5):
            lines.append(f.readline())
        f.readline() # skip empty line
        print test(lines, case)

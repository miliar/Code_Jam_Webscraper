def solution(parsed_line):
    all_s = ''.join(parsed_line)

    def is_winning(line):
        if line.count('X') == 4:
            return 'X won'
        if line.count('O') == 4:
            return 'O won'
        if line.count('X') == 3:
            if 'T' in line:
                return 'X won'
        if line.count('O') == 3:
            if 'T' in line:
                return 'O won'
        return -1

    # horizontal
    for i in range(4):
        q = is_winning(parsed_line[i])
        if q != -1:
            return q

    for i in range(4):
        l = []
        for j in range(4):
            l.append(parsed_line[i][j])
        q = is_winning(l)
        if q != -1:
            return q
    # diagonal

    test_l1 = [parsed_line[i][i] for i in range(4)]
    q = is_winning(test_l1)
    if q != -1:
        return q
    test_l2 = [parsed_line[i][3 - i] for i in range(4)]
    q = is_winning(test_l2)
    if q != -1:
        return q
    if '.' not in all_s:
        return 'Draw'
    return 'Game has not completed'
    
def parse_input(f):
    data = open(f).read().split("\n")
    result = []
    T = int(data[0])

    for i in range(1, len(data) - 1):
        if (i % 5) == 1:
            result.append([])
        if (i % 5) != 0:
            result[-1].append(data[i])
    return result

def solve():
    process_output = lambda l: l

    f = 'A-small-attempt2.in'
    fout = open('output.txt', 'w')
    parsed_input = parse_input(f)

    for line in range(len(parsed_input)):
        print '\n'.join(parsed_input[line]) + '\n'
        print solution(parsed_input[line]) + '\n'
        s = "Case #" + str(line + 1) + ": " + process_output(solution(parsed_input[line])) + "\n"
        fout.write(s)

    fout.close()

solve()


def input_list(file_name):
    test = []
    with open(file_name, 'r') as reader:
        T = int(next(reader).strip())
        for ind in range(T):
            line = next(reader)
            strs = line.strip().split(' ')
            tu = (strs[0], int(strs[1]))
            test.append(tu)
    return test


def print_line(ind, r):
    return 'Case #{}: {}\n'.format(ind, r)


def count_flip(S, K):
    if '-' in S:
        head = S.index('-')
        tail = head + K
    else:
        return 0

    flip = 0
    while tail <= len(S):
        flip += 1
        for i in range(head, tail):
            S[i] = '+' if S[i] == '-' else '-'

        if '-' in S:
            head = S.index('-')
        else:
            return flip

        tail = head + K

    return 'IMPOSSIBLE'


if __name__ == '__main__':
    test_list = input_list('A-large.in')
    f = open('A-large.out', 'w')
    ind = 1
    for S, K in test_list:
        flip = count_flip(list(S), K)
        f.write(print_line(ind, flip))  # python will convert \n to os.linesep
        ind += 1
    f.close()


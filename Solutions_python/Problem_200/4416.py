def read_input(file_name):
    with open(file_name, 'r') as f:
        lines = f.read().splitlines()
        nr_of_cases = int(lines[0])
        cases = [int(line) for line in lines[1:]]
    return nr_of_cases, cases


def find_biggest_tidy_number(nr):
    nr_as_list = [int(i) for i in str(nr)]
    # reverse order for easier handling
    l = nr_as_list[::-1]

    for i in range(len(l)-1):

        if l[i+1] <= l[i]:
            pass
        else:
            l[i+1] -= 1
            l[i] = 9
            for j in range(i):
                l[j] = 9

    # reverse order back to normal
    right_order = l[::-1]

    return int(''.join(str(x) for x in right_order))


if __name__ == '__main__':
    nr, cases = read_input('B-large.in')
    for i in range(nr):
        print('Case #{}: {}'.format(i+1, find_biggest_tidy_number(cases[i])))
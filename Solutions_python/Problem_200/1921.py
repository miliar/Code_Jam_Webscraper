import os


def read_file(filename):
    path = os.path.join('inputs', filename)
    with open(path, 'r') as f:
        return f.readlines()


def write_file(filename, content):
    path = os.path.join('outputs', filename + '.out')
    with open(path, 'w+') as f:
        return f.writelines(content)


def main():
    for in_file in os.listdir('inputs'):
        content = read_file(in_file)
        result = algo(content)
        write_file(in_file, result)


def algo(content):
    size = int(content[0])
    inputs = [map(int, list(line.strip())) for line in content[1:1+size]]

    return [format_(i, solution(case)) for i, case in enumerate(inputs)]


def format_(i, s):
    return "Case #{}: {}".format(i + 1, s)

def solution(case):
    while not is_tidy(case):
        case = roll_next_unit(case)
    case = remove_zeros(case)
    return "".join(map(str, case)) +  "\n"

def is_tidy(l):
    return all(l[i] <= l[i+1] for i in xrange(len(l)-1))


def roll_next_unit(case):

    i = len(case) - 1
    while i > 0:
        if int(case[i]) < int(case[i-1]):
            print case, i
            case[i] = 9
            case[i - 1] -= 1
            j = 0
            while i - 1 - j > 0 and case[i - 1 - j] == -1:
                case[i - 1 - j] = 0
                case[i - 1 - j - 1] -= 1
                j += 1
            j = 1
            while i - 1 + j < len(case):
                case[i - 1 + j] = 9
                j += 1
            return case
        i -= 1
    return case


def remove_zeros(case):
    if len(case) == 1:
        return case
    i = 0
    while (i < len(case)) and case[i] == 0:
        i+= 1
    return case[i:]

if __name__ == '__main__':
    main()

# pylint: disable=missing-docstring
import sys


def problem(groups, pieces):
    fresh = 1
    groups = [x % pieces for x in groups]
    fresh += groups.count(0)
    groups = [x for x in groups if x != 0]

    for a in range(pieces):
        while True:
            b = pieces - a
            if a == b and groups.count(a) >= 2:
                groups.remove(a)
                groups.remove(b)
                fresh += 1
            elif a != b and a in groups and b in groups:
                groups.remove(a)
                groups.remove(b)
                fresh += 1
            else:
                break
    assert not (1 in groups and 3 in groups)
    assert not (1 in groups and 2 in groups and pieces == 3)
    assert not (pieces == 4 and groups.count(2) > 4)
    if groups.count(2) == 1 and pieces == 4:
        if len(groups) >= 3:
            groups.remove(2)
            del groups[-1]
            del groups[-1]
            fresh += 1
        else:
            return fresh

    while len(groups) >= pieces:
        for i in range(pieces):
            del groups[-1]
        fresh += 1


    if not groups:
        return fresh - 1
    return fresh


def nextline(input_file):
    data = ""
    while not data:
        data = input_file.readline()
    return data[:-1]

def intsplit(s):
    return [int(x) for x in s.split(" ")]


def main():
    result = ""
    with sys.stdin if len(sys.argv) == 1 else open(sys.argv[1], 'r') as infile:
        number = int(nextline(infile))
        for run in range(number):
            case = nextline(infile)
            numGroups, pieces = intsplit(case)
            groups = intsplit(nextline(infile))
            result += 'Case #{}: {}\n'.format(1 + run, problem(groups, pieces))

    if len(sys.argv) == 1:
        print(result, end='')
    else:
        with open(sys.argv[1].replace('in', 'sol'), 'w') as result_file:
            result_file.write(result)

if __name__ == '__main__':
    main()

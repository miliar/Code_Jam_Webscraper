#! /usr/bin/python
import sys


def inver(lines):
    new_lines = []
    line = ""
    for i in range(4):
        for j in range(4):
            line += lines[j][i]
        new_lines.append(line)
        line = ""
    return new_lines


def get_diagon(lines):
    new_lines = []
    line = ""
    for i in range(4):
        line += lines[i][i]
    new_lines.append(line)

    line = ""
    for i in range(4)[::-1]:
        line += lines[3 - i][i]
    new_lines.append(line)
    return new_lines


def search(lines, case):
    is_draw = True
    chars = ('X', 'O')
    valid_lines = [lines, inver(lines), get_diagon(lines)]

    for char in chars:
        for lines in valid_lines:
            for line in lines:
                line = line.replace('T', char)
                if str(char) * 4 in line:
                    return r'Case #%d: %s won' % (case, char)
            if '.' in line:
                is_draw = False
    return "Case #%d: %s" % (
        case, "Draw" if is_draw else "Game has not completed")


def main(argv=sys.argv):
    case = 1
    counter = 0
    file_name = argv[1]
    f = open(file_name, 'r')
    output = open("output.txt", 'w')
    lines = []

    for line in f.readlines():
        line = line.replace('\n\n', '\n \n').replace('\n', '')
        if line != '6' and line != '10' and line != '':
            if counter < 4:
                lines.append(str(line))
                counter += 1

            if counter == 4:
                result = search(lines, case)
                print result
                output.write("%s\n" % result)
                case += 1
                counter = 0
                lines = []
    f.close()
    output.close()


if __name__ == "__main__":
    main()

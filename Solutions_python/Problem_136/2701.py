# Cookie Clicker Alpha
# Joseph Lee <joe.lee.three.thousand@gmail.com>
# Google Code Jam 2014
# Preliminary Round

from sys import argv


def test_case(line):
    rate = 2.0
    elapsed = 0.0
    c, f, x = map(float, line.strip().split(' '))

    current_estimate = x / rate
    farm_purchase_estimate = (c / rate) + (x / (rate + f))

    while farm_purchase_estimate < current_estimate:
        elapsed += c / rate
        rate += f
        current_estimate = x / rate
        farm_purchase_estimate = (c / rate) + (x / (rate + f))

    return '%.7f' % (elapsed + (x / rate))



def main():
    input_fname = argv[1]
    with open(input_fname, 'r') as input_file:
        raw_lines = input_file.readlines()
    raw_lines.pop(0)    # test cases, unnecessary

    case_num = 1
    for line in raw_lines:
        print 'Case #%d: %s' %(case_num, test_case(line))
        case_num += 1


if __name__ == '__main__':
    main()

import sys
import math

def is_palendrome(number):
    number_string = str(number)
    return number_string == number_string[::-1]

def main(argv):
    if len(argv) != 2:
        sys.exit('Usage: python filename.py <input_file> <output_file>')
    with open(argv[0], 'r') as data, open(argv[1], 'w+') as output:
        lines = map(lambda s: s.strip(), data.readlines())
        case = 1
        for line in lines[1:]:
            solution = 0
            range_list = map(int, line.split())
            lower_range_square = int(math.sqrt(range_list[0]-1)) + 1
            upper_range_square = int(math.sqrt(range_list[1]))
            for i in range(lower_range_square, upper_range_square + 1):
                if is_palendrome(i) and is_palendrome(i**2):
                    solution += 1;
            output.write("Case #{}: {}\n".format(case, solution))
            case += 1
    data.close()
    output.close()

if __name__ == '__main__':
    main(sys.argv[1:])

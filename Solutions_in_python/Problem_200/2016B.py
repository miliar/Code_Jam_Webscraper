import sys


def solve(N):

    if N < 10:
        return N

    num_str = str(N)

    for i in range(1, len(num_str)):
        if int(num_str[i]) < int(num_str[i-1]):
            j = i-1
            while j > 0 and int(num_str[j]) == int(num_str[j-1]):
                j -= 1
            j += 1
            part_1 = num_str[:j]
            part_2 = num_str[j:]
            new_str = part_1 + '0' * len(part_2)
            return int(new_str) - 1

    return N



def process_file(input_file, output_file):
    file_in = open(input_file, 'rU')
    file_out = open(output_file, 'w')

    
    i = 0
    num_cases = None
    case_num = 0
    answer_1 = None
    answer_2 = None
    card_set_1 = None
    card_set_2 = None

    for row in file_in:
        
        if not num_cases:
            num_cases = int(row)

        else:
            case_num += 1
            result = solve(int(row))
            res_string = 'Case #%i: %i' % (case_num, result)
            # print(res_string)
            file_out.write(res_string + '\n')

    file_out.close()
            

def main():
    if len(sys.argv) == 3:
        print('Program starts')
        process_file(sys.argv[1], sys.argv[2])
        print('Done')
        sys.exit(1)
        
    else:
        print('Give two arguments (INPUT_FILE OUTPUT_FILE)')
        sys.exit(1)


if __name__ == '__main__':
    main()

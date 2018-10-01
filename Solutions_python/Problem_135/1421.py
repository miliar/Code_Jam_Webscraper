__author__ = 'nik'


def parse_input_file():
    pass


def main():
    output_file = open('output', 'w')
    with open('input') as input_file:
        next(input_file)
        i = 0
        case_num = 0
        row1_number = 100
        row2_number = 100
        for line in input_file:
            if i == 0:
                row1_number = line
            if int(row1_number) == i:
                row1 = line
                row1 = row1.split(' ')
                row1 = map(int, row1)
            if i == 5:
                row2_number = line
            if int(row2_number) + 5 == i:
                row2 = line
                row2 = row2.split(' ')
                row2 = map(int, row2)
            i += 1
            if i == 10:
                i = 0
                row1_number = 100
                row2_number = 100
                result = set(row1) & set(row2)
                case_num += 1
                if len(result) == 1:
                    output = 'Case #' + str(case_num) + ': ' + str(result.pop())+'\n'
                elif len(result) > 1:
                    output = 'Case #' + str(case_num) + ': Bad magician!'+'\n'
                else:
                    output = 'Case #' + str(case_num) + ': Volunteer cheated!'+'\n'
                output_file.write(output)
                print output


if __name__ == '__main__': main()
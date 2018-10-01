LINES_PARAM = 0
INPUT_FILE_NAME = 'A-large.in'
OUTPUT_FILE_NAME = 'A-large.out'

def noInit(line):
    return line==len(line)*'?'
def splitline(line):
    result=['' for i in range(len(line))]
    found=False
    empty=0
    for i in range(len(line)):
        if (line[i]=='?'):
            if found:
                result[i]=result[i-1]
            else:
                empty+=1
        else:
            result[i]=line[i]
            found=True
    for i in range(empty):
        result[i]=result[empty]
    return ''.join(result)
def do_case(parsed):
    result=['' for i in range(len(parsed))]
    found=False
    empty=0
    for i in range(len(parsed)):
        if noInit(parsed[i]):
            if found:
                result[i]=result[i-1]
            else:
                empty+=1
        else:
            result[i]=splitline(parsed[i])
            found=True
    for i in range(empty):
        result[i]=result[empty]
    return '\n'.join(result)


def do_parse(input):
    s= [line.rstrip() for line in input]
    return s[1:]


def main():
    input_f = open(INPUT_FILE_NAME, 'r')
    output = []

    num_of_test_cases = int(input_f.readline(), 10)
    temp = input_f.readlines()
    index = 0
    for test_case in range(num_of_test_cases):
        lines = int(temp[index].rstrip().split(" ")[LINES_PARAM])
        parsed_input = do_parse(temp[index:index + lines + 1])
        index = index + 1 + lines
        output.append('Case #' + str(test_case + 1) + ': \n' + do_case(parsed_input))

    output_f = open(OUTPUT_FILE_NAME, 'w')
    output_f.write('\n'.join(output))

    input_f.close()
    output_f.close()


if __name__ == '__main__':
    main()

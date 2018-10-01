import math
LINES_PARAM = 0
INPUT_FILE_NAME = 'B-small-attempt0.in'
OUTPUT_FILE_NAME = 'B-small-attempt0.out'

def arekit(sizes,recipe):
    M=max([math.ceil(sizes[i]/(1.1*recipe[i])) for i in range(len(sizes))])
    m=min([math.floor(sizes[i]/(0.9*recipe[i])) for i in range(len(sizes))])
    return m>=M
def do_case(parsed):
    N=parsed[0][0]
    P=parsed[0][1]
    recipe=parsed[1]
    packages=[sorted(packs) for packs in parsed[2:]]
    counters=[0 for i in range(N)]
    result =0
    while(max(counters)<P):
        if arekit([packages[i][counters[i]] for i in range(N)],recipe):
            result+=1
            counters=[i+1 for i in counters]
        else:
            ratios=[1.0*packages[i][counters[i]]/recipe[i] for i in range(N)]
            m=ratios.index(min(ratios))
            counters[m]+=1
    return str(result)


def do_parse(input):
    return [[int(num) for num in line.rstrip().split(" ")]for line in input]


def main():
    input_f = open(INPUT_FILE_NAME, 'r')
    output = []

    num_of_test_cases = int(input_f.readline(), 10)
    temp = input_f.readlines()
    index = 0
    for test_case in range(num_of_test_cases):
        lines = int(temp[index].rstrip().split(" ")[LINES_PARAM])
        parsed_input = do_parse(temp[index:index + lines + 2])
        index += 2 + lines
        output.append('Case #' + str(test_case + 1) + ': ' + do_case(parsed_input))

    output_f = open(OUTPUT_FILE_NAME, 'w')
    output_f.write('\n'.join(output))

    input_f.close()
    output_f.close()


if __name__ == '__main__':
    main()

import sys


def process(input, result_file):
    t = int(input[0])
    for case in range(1, t + 1):
        last = [int(digit) for digit in list(input[case].strip())]
        ln = len(last)

        for i in range(ln - 1, 0, -1):
            if last[i] < last[i-1]:
                last[i-1] -= 1
                last[i:] = [9] * (ln-i)
            #print(i, last[i], last)

        result = int(''.join((str(digit) for digit in last)))

        result_string = "Case #{}: {}".format(case, result)
        print(result_string)
        result_file.write(result_string + "\n")


if __name__ == "__main__":
    # input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    # This is all you need for most Google Code Jam problems.
    file_name = sys.argv[1]
    result_file_name = file_name + "_result"
    with open(result_file_name, 'w') as result_file:
        with open(file_name) as input_file:
            content = input_file.readlines()
        process(content, result_file)
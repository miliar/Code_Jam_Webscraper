

def get_starting_tidy_substr_index(number_str):
    index = 0
    last_tidy_digit = int(number_str[index])
    for index in range(1, len(number_str)):
        if int(number_str[index]) >= last_tidy_digit:
            last_tidy_digit = int(number_str[index])
        else:
            return index - 1
    return index


def get_largest_smaller_tidy(number_str):

    index = get_starting_tidy_substr_index(number_str)

    if index == len(number_str) - 1:
        return number_str

    last_tidy_digit = number_str[index]
    starting_nines_index = index
    for i in range(index, -1, -1):
        if last_tidy_digit != number_str[i]:
            break
        starting_nines_index = i

    last_tidy_digit = int(number_str[starting_nines_index])
    remaining_str_len = len(number_str[starting_nines_index + 1:])
    output = number_str[:starting_nines_index] + str(last_tidy_digit - 1) + remaining_str_len * '9'
    if output[0] == '0':
        return output[1:]
    return output

if __name__ == "__main__":

    output = open("B-large.out", "w")

    with open("B-large.in", "r") as input_file:
        cases = int(input_file.readline())
        for i in range(0, cases):
            input_case = input_file.readline().replace('\n','')
            result = get_largest_smaller_tidy(input_case)
            output.write("Case #{}: {}\n".format(i + 1, result))

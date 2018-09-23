# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
def formatted(answer, curr_case):
    return 'Case #{}: {}'.format(curr_case, answer)

def answer(line):
    line = line.split(' ')
    input_list = list(line[0])
    ##print(input_list)
    flipper_size = int(line[1])
    possible_flip_locations = len(input_list) - flipper_size + 1
    number_of_flips = 0

    for key in range(possible_flip_locations):
        if input_list[key] == '-':
            number_of_flips += 1
            for place in range(flipper_size):
                if input_list[key + place] == '-':
                    input_list[key + place] = '+'
                else:
                    input_list[key + place] = '-'

    if '-' in input_list[1 - flipper_size:]:
        return 'IMPOSSIBLE'
    else:
        return number_of_flips

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    line = input()
    print(formatted(answer(line), i))

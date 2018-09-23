##########################
#  Google Code Jam 2017  #
#     Bathroom Stalls    #
# Written by Jake Herman #
##########################

def create_bathroom(num_of_stalls: int) -> list:
    result = [1]
    for x in range(num_of_stalls):
        result.append(0)
    result.append(1)
    return result

def find_gap(bathroom: list) -> list:
    cur_stall = 0
    largest_gap = [0, 0]

    gap_start = 0

    for stall in bathroom:
        if stall == 1:
            gap_end = cur_stall

            if (gap_end - gap_start) > (largest_gap[1] - largest_gap[0]):
                largest_gap[0] = gap_start
                largest_gap[1] = gap_end

            gap_start = cur_stall

        cur_stall += 1

    return largest_gap

def sit_in_stall(bathroom: list, gap: list) -> list:
    bathroom[gap[0] + int((gap[1] - gap[0]) / 2)] = 1
    return bathroom

def find_last_stall(stalls: int, people: int) -> (int, int):
    bathroom = create_bathroom(stalls)

    for person in range(people - 1):
        bathroom = sit_in_stall(bathroom, find_gap(bathroom))

    final_gap = find_gap(bathroom)
    final_stall = final_gap[0] + int((final_gap[1] - final_gap[0]) / 2)
    left_space = 0
    right_space = 0

    for stall in bathroom[final_stall + 1:]:
        if stall == 0:
            right_space += 1
        else:
            break

    for stall in reversed(bathroom[:final_stall]):
        if stall == 0:
            left_space += 1
        else:
            break

    return (left_space, right_space)

def generate_file(file: open):
    file.readline()
    case_num = 1

    for case in file.readlines():
        case = case.strip("\n")
        split_str = case.split(' ')
        result = find_last_stall(int(split_str[0]), int(split_str[1]))

        print("Case #{}: {} {}".format(case_num, max(result), min(result)))
        case_num += 1

if __name__ == '__main__':
    generate_file(open("C-small-1-attempt0.in"))
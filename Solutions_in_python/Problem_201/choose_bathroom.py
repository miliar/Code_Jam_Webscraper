def read_inputs():
    t = int(input())  # read a line with a single integer
    case_set = []
    for i in range(1, t + 1):
        n, m = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
        case_set.append((n,m))
    return case_set

def find_weight(start, end, stall_list):
    return sum(stall_list[start:end])
    
def bin_search_stall(start, end, stall_list):

    my_stall = int((end+start)/2)

    if start == end:
        print(stall_list)
        print(len(stall_list))
        exit()

    if stall_list[my_stall] == 1:
        # if L > R, go R, else go L
        if find_weight(start, my_stall, stall_list) > find_weight(my_stall+1, end, stall_list):
            return bin_search_stall(my_stall, end, stall_list)
        else:
            return bin_search_stall(start, my_stall, stall_list)
    else:
        stall_list[my_stall] = 1
        return stall_list, my_stall

def find_closest_left_right(stalls, my_stall):
    closest_left = 0
    closest_right = my_stall

    for index in range(len(stalls)):
        if index < my_stall and stalls[index] == 1:
            closest_left = index
        elif index > my_stall and stalls[index] == 1:
            closest_right = index
            break

    return closest_left, closest_right

def print_output(results):
    for i in range(len(results)):
        print('Case #{0}: {1}'.format(i+1, 
                                            str(results[i]).replace('(', ''
                                                    ).replace(')', ''
                                                    ) .replace(',', '')
                                                ) 
                )

cases = read_inputs()
result = []

for num_stalls, num_people in cases:
   
    stalls = [0 for i in range(num_stalls+2)]
    stalls[0], stalls[-1] = 1, 1

    start_stall, end_stall = 0, len(stalls) -1
    occupied_stall = 0

    for people  in range(num_people):
        stalls, occupied_stall = bin_search_stall(start_stall, end_stall, stalls)

    closest_left, closest_right = find_closest_left_right(stalls, occupied_stall)

    d2left = occupied_stall - closest_left -1
    d2right = closest_right - occupied_stall -1

    result.append((max(d2left, d2right), min(d2left, d2right)))

print_output(result)

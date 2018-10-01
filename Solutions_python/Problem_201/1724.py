input_file = open('/Users/eunice.lin/Downloads/C-small-1-attempt1.in', 'r')


num_cases = input_file.readline()

i = 1
n = 0
result = ''

def get_largest_range_indices(occupied, n):
    max_range = 0
    max_left = 0
    max_right = 0
    for i in range(len(occupied)-1):
        stalls = occupied[i+1] - occupied[i]
        if stalls > max_range:
            max_range = stalls
            max_left = occupied[i]
            max_right = occupied[i+1]
    return max_left, max_right


for line in input_file:
    n, k = line.split(" ")
    n = int(n)
    k = int(k)
    occupied = [0, n+1]
    for x in range(k):
        left, right = get_largest_range_indices(occupied, n)
        current = (left+right)/2
        if not current in occupied:
            occupied.append(current)
            occupied.sort()
        else:
            result += "Case #{}: {} {}\n".format(i, max_dist, min_dist)
            break
        
    left_dist = 0
    right_dist = 0
    if current-left > 0:
        left_dist = current-left-1
    if right-current> 0:
        right_dist = right-current-1
    max_dist = max(left_dist, right_dist)
    min_dist = min(left_dist, right_dist)
    result += "Case #{}: {} {}\n".format(i, max_dist, min_dist)
    i += 1

output_small = open('./C-result-small.txt', 'w+')
output_small.write(result)



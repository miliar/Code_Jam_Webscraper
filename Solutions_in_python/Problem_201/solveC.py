import math
import sys

def read_data(filename):
    with open(filename) as f:
        cases = int(f.readline().strip())
        data = []
        for i in xrange(cases):
            N, K = map(int, f.readline().strip().split())
            data.append((N, K))
        return data

def level_distribution(total, level):
    base = total / (2 ** level)
    offset = total - (base * (2 ** level) + (2 ** level - 1))
    if offset < 0:
        offset *= -1
        other = base - 1
        result = (base, (2 ** level) - offset), (other, offset)
    else:
        other = base + 1
        result = (other, offset), (base, (2 ** level) - offset)
    return result

def calculate_position(num_stalls):
    if num_stalls == 1:
        return (0, 0)
    num_stalls = num_stalls - 1
    return num_stalls / 2, (num_stalls / 2) + (num_stalls % 2)


def stalls(data):
    case_num = 1
    for stalls, people in data:
        level = int(math.log(people, 2))

        level_dist = level_distribution(stalls, level)

        people_in_level = people - ((2 ** level) - 1)
        # print level_dist, stalls, people, level, people_in_level
        if level == 0:
            result = calculate_position(stalls)
        elif people_in_level <= level_dist[0][1]:
            result = calculate_position(level_dist[0][0])
        else:
            result = calculate_position(level_dist[1][0])

        print "Case #{}: {} {}".format(case_num, max(result), min(result))
        case_num += 1


if __name__ == '__main__':
    file_name = sys.argv[1]

    stalls(read_data(file_name))

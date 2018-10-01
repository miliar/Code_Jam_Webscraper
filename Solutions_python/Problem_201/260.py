from itertools import count
from collections import defaultdict

def get_index(stall_count):
    return stall_count // 2

def split_stalls(stall_count, index):
    return index, stall_count - index - 1


def case(number_of_stalls, number_of_people):
    stall_sections = []
    counts = defaultdict(lambda: 0)
    def add(section, count):
        nonlocal stall_sections
        if section not in stall_sections:
            stall_sections.append(section)
            stall_sections = sorted(stall_sections, reverse=True)
        counts[section] += count
        return stall_sections
        
    index = None
    section = number_of_stalls
    add(section, 1)

    while number_of_people > 0:
        #print([(k,counts[k]) for k in stall_sections ])
        section = stall_sections.pop(0)
        count = counts.pop(section)

        index = get_index(section)
        left, right = split_stalls(section, index)
        stall_sections = add(left, count)
        stall_sections = add(right, count)

        number_of_people -= count

    final_split = split_stalls(section, index)
    return max(final_split), min(final_split)


def cases(data):
    lines = int(data[0])
    for case_number, line in zip(count(1), data[1:]):
        n, k = line.split(' ')
        result = case(int(n), int(k))
        print("Case #{}: {} {}".format(case_number, *result))

with open('input', 'r') as f:
    cases(f.readlines())

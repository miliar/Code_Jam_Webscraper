import math
from sortedcontainers import SortedList
from collections import defaultdict


def get_children(parent_int):

    if parent_int % 2 == 0:
        return int(parent_int/2), int(parent_int/2 - 1)
    else:
        return int(math.floor(parent_int/2)), int(math.floor(parent_int/2))


def calculate_number(empty_stalls, users):
    tree_array = SortedList()
    tree_array.add(empty_stalls)
    child1 = None
    child2 = None
    for j in range(0, users):
        child1, child2 = get_children(tree_array.pop())
        tree_array.add(child1)
        tree_array.add(child2)
    return child1, child2


def get_tree(root_value, tree_level):
    d = [{root_value: 1}]
    for i in range(0, tree_level):
        next_level = defaultdict(lambda: 0)
        for key in d[i]:
            child1, child2 = get_children(key)
            next_level[child1] += d[i][key]
            next_level[child2] += d[i][key]
        d.append(dict(next_level))
    return d


def calculate_number_with_log(empty_stalls, users):

    tree_level = math.floor(math.log(users, 2))
    position_in_leafs = users - ( math.pow(2, tree_level) - 1)
    max_value_in_leafs = math.floor(empty_stalls/math.pow(2, tree_level))
    tree = get_tree(empty_stalls, int(tree_level))
    leaves = tree[-1]

    if leaves[max_value_in_leafs] >= position_in_leafs:
        current_value = max_value_in_leafs
    else:
        current_value = max_value_in_leafs - 1

    return get_children(current_value)


if __name__ == "__main__":

    output = open("C-small-2.out", "w")

    with open("C-small-2-attempt1.in", "r") as input_file:
        cases = int(input_file.readline())
        for i in range(0, cases):
            input_line = input_file.readline().replace('\n','')
            input_values = tuple(int(i) for i in input_line.split(' '))
            ls, rs = calculate_number_with_log(input_values[0], input_values[1])
            output.write("Case #{}: {} {}\n".format(i + 1, ls, rs))



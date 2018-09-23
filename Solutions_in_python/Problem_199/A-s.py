import sys

flip_char = lambda x: '-' if x == '+' else '+'

def flip(pancakes, fr, k):
    return pancakes[:fr] + ''.join(map(flip_char, pancakes[fr:fr+k])) + pancakes[fr+k:]


def solve(pancakes, flipper_size):
    pancakes_size = len(pancakes)
    target = '+' * pancakes_size
    flip_target = '+' * flipper_size
    current_steps = 0
    current_set = {pancakes}
    next_set = set()
    closed_set = set()
    while True:
        if current_set:
            current_pancake = current_set.pop()
            if current_pancake == target:
                return current_steps
            closed_set.add(current_pancake)
            for i in range(pancakes_size - flipper_size + 1):
                if current_pancake[i:i + flipper_size] != flip_target:
                    new_pancake = flip(current_pancake, i, flipper_size)
                    if new_pancake not in closed_set and new_pancake not in current_set:
                        next_set.add(new_pancake)

        elif next_set:
            current_set, next_set = next_set, set()
            current_steps += 1
        else:
            return "IMPOSSIBLE"


if len(sys.argv) != 3:
    print("Use: {} <input_file> <output_file>".format(sys.argv[0]))
    exit(1)

input_filename, output_filename = sys.argv[1], sys.argv[2]
in_file = open(input_filename, 'r')
out_file = open(output_filename, 'w')
test_cases = int(in_file.readline())
for i in range(test_cases):
    pancakes, flipper_size = in_file.readline().split()
    result = solve(pancakes, int(flipper_size))
    out_file.write("Case #{}: {}\n".format(i+1, result))
in_file.close()
out_file.close()

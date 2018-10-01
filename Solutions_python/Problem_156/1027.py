import math
import copy
# Checking if recursive library import causes issue.

class Plates(object):
    def __init__(self, plates):
        self.plates = {}
        for plate_count in plates:
            if plate_count not in self.plates:
                self.plates[plate_count] = 1
            else:
                self.plates[plate_count] += 1

    def is_eaten(self):
        if self.plates != {}:
            return False
        else:
            return True

    def _add_stacks(self, stack_height, number_plates):
        if stack_height not in self.plates:
            self.plates[stack_height] = number_plates
        else:
            self.plates[stack_height] += number_plates

    def get_new_eat_plates(self):
        new_plates = Plates([])
        for height, number_plates in self.plates.items():
            if height == 1:
                pass
            else:
                new_plates._add_stacks(height - 1, number_plates)
        return new_plates

    def get_new_split_plates(self):
        new_plates = Plates([])

        biggest_stack_height = max(self.plates.keys())
        biggest_stack_count = self.plates[biggest_stack_height]

        if biggest_stack_height == 1:
            return new_plates

        if biggest_stack_height != 9:
            smaller_height = int(math.floor(biggest_stack_height / 2.0))
            larger_height = int(math.ceil(biggest_stack_height / 2.0))
        else:
            smaller_height = biggest_stack_height / 3
            larger_height = 2 * biggest_stack_height / 3

        new_plates._add_stacks(stack_height=smaller_height, number_plates=1)
        new_plates._add_stacks(stack_height=larger_height, number_plates=1)

        for stack_height, number_plates in self.plates.iteritems():
            if stack_height == biggest_stack_height:
                if number_plates == 1:
                    pass
                else:
                    # We split one stack.
                    new_plates._add_stacks(stack_height=stack_height, number_plates=number_plates-1)
            else:
                new_plates._add_stacks(stack_height=stack_height, number_plates=number_plates)

        return new_plates


def parse_input(file_name):
    with open(file_name) as f:
        lines = f.readlines()

    num_cases = int(lines[0])

    cases = []

    for case_number in range(0, num_cases*2, 2):
        first_idx = case_number + 1
        second_idx = case_number + 2

        num_plates = int(lines[first_idx].strip("\n"))
        plate_vals = [int(val) for val in lines[second_idx].strip("\n").split(" ")]

        cases.append((num_plates, plate_vals))

    return cases


def solve_one_case(case):
    fringe = []

    num_plates, plate_vals = case

    print plate_vals
    fringe.append((0, Plates(plate_vals)))

    minimum = 100000
    while fringe:
        number_moves, plates = fringe.pop(0)

        new_eat_plates = plates.get_new_eat_plates()
        new_split_plates = plates.get_new_split_plates()

        if new_split_plates.is_eaten() or new_eat_plates.is_eaten():
            if (number_moves + 1) < minimum:
                minimum = number_moves + 1

        if not new_split_plates.is_eaten():
            fringe.append((number_moves + 1, new_split_plates))

        if not new_eat_plates.is_eaten():
            fringe.append((number_moves + 1, new_eat_plates))

    return minimum
    raise Exception("No result found, we have a bug.")


def write_output(solved_cases):
    lines = []
    for case_idx, case in enumerate(solved_cases):
        line = "Case #{}: {}".format(case_idx + 1, case)
        lines.append(line)
    with open("output.txt", "w") as f:
        f.write("\n".join(lines))

    with open("output.txt") as f:
        print(f.read())


def solve_all(file_name):
    cases = parse_input(file_name)
    solved_cases = []
    for case in cases:
        solved_case = solve_one_case(case)
        solved_cases.append(solved_case)

    write_output(solved_cases)
    import pprint
    pprint.pprint(zip(cases, solved_cases))

# print(parse_input("./test_input.txt"))
# print(solve_all("./test_input.txt"))
# print(solve_all("/home/tim/Downloads/B-small-attempt5.in"))

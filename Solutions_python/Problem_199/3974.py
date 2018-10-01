def add_case_line(file_path, case_index, string):
    with open(file_path, "a") as f:
        f.write("Case #{}: {}\n".format(case_index, string))


def flip_pancakes(pancakes_conf, index, flipper_size):
    length = len(pancakes_conf)
    if index > length - flipper_size:
        index = length - flipper_size
    return_value = list(pancakes_conf)
    for i in range(index, index+flipper_size):
        pancake = return_value[i]
        return_value[i] = '-' if pancake == '+' else '+'
    return return_value


def calculate_solution_internal(pancakes_conf, flipper_size, n_moves, tried_solutions):
    tried_solutions.append(pancakes_conf)
    if "-" not in pancakes_conf:
        return True, n_moves
    last_index = -1
    min_moves = -1
    any_solved = False
    while True:
        try:
            index = pancakes_conf.index('-', last_index + 1)
            flipped_pancakes = flip_pancakes(pancakes_conf, index, flipper_size)
            if flipped_pancakes not in tried_solutions:
                r_solved, r_n_moves = calculate_solution_internal(flipped_pancakes, flipper_size, n_moves+1, tried_solutions)
                if r_solved:
                    any_solved = True
                    min_moves = r_n_moves if min_moves == -1 or r_n_moves < min_moves else min_moves
            last_index = index
        except ValueError:
            break
    return any_solved, min_moves


def calculate_solution(pancakes_conf, flipper_size):
    return calculate_solution_internal(pancakes_conf, flipper_size, 0, list())


def run(file_rel_path, out_rel_path):
    import os
    curr_path = os.path.dirname(os.path.abspath(__file__))
    input_file_path = "{}/{}".format(curr_path, file_rel_path)
    output_file_path = "{}/{}".format(curr_path, out_rel_path)
    with open(input_file_path, "r") as input_file:
        with open(output_file_path, "w"):
            pass
        lines = input_file.readlines()
        i = 1
        for line in lines[1:]:
            line = line.strip("\n")
            parts = line.split(" ")
            pancakes_conf = list(parts[0])
            flipper_size = int(parts[1])
            solution, n_moves = calculate_solution(pancakes_conf, flipper_size)
            add_case_line(output_file_path, i, "IMPOSSIBLE" if not solution else str(n_moves))
            i += 1


if __name__ == "__main__":
    #file = "example"
    file = "A-small-attempt0"
    run("input/a/{}.in".format(file), "output/a/{}.txt".format(file))

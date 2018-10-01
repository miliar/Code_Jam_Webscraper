
import time

g_round = ""
g_question = "A"
# g_step = "sample"
g_step = "small-attempt0"
# g_step = "large"

g_file_in = g_question + "-" + g_step + ".in"
g_file_out = g_question + "-" + g_step + ".out" + "." + str(time.time())

g_problem_start = 0
g_problem_end = -1

g_validate = True


def error(message):
    import inspect, logging
    # Get the previous frame in the stack, otherwise it would be this function!!!
    func = inspect.currentframe().f_back.f_code
    # Dump the message + the name of this function to the log.
    logging.error("%s: %s in %s:%i" % (
        message,
        func.co_name,
        func.co_filename,
        func.co_firstlineno
    ))


def validate(problem, result):
    if not g_validate:
        return




### start

# import re


def happy(pancake):
    for c in pancake:
        if c == '-':
            return False
    return True


def flip_over(pancake):
    result = ""
    for c in pancake:
        if c == '+':
            result += '-'
        else:
            result += '+'
    return result


def flip(pancake, size, n_flips, start, end):

    print("F {}".format([("+"*start) + pancake, n_flips, size, start]))

    if happy(pancake):
        return pancake, n_flips

    if size > len(pancake):
        return pancake, -1

    sub_cake = pancake
    front_pos = pancake.find("-")
    if front_pos >= 0:
        if front_pos + size > len(pancake):
            return pancake, -1
        sub_cake = flip_over(pancake[front_pos:front_pos+size]) + pancake[front_pos+size:]

        if len(sub_cake) + front_pos != len(pancake):
            error([sub_cake, front_pos])

        return flip(sub_cake, size, n_flips + 1, start + front_pos, end)

    else:
        return pancake, n_flips

### end


def solve(problem):

    pancake, size_str = problem.split(' ')

    output, number = flip(pancake, int(size_str), 0, 0, len(pancake))

    if number < 0:
        return "IMPOSSIBLE"
    return str(number)

f_out = open(g_file_out, 'w')

def run():
    with open(g_file_in) as f_in:
        num_problems = int(f_in.readline())
        i_line = 0
        for line in f_in:
            i_line += 1
            if line[-1] == '\n':
                line = line[:-1]
            problem = line

            print(i_line)

            result = solve(problem)
            f_out.write("Case #{}: {}".format(i_line, result))
            f_out.write('\n')


run()

f_out.close()
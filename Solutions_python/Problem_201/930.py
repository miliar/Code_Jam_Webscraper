
import time
import sys

g_round = ""
g_question = "C"
# g_step = "sample"
# g_step = "small-2-attempt0"
g_step = "large"

g_file_in = g_question + "-" + g_step + ".in"
g_file_out = g_question + "-" + g_step + ".out" + "." + str(time.time())

g_problem_start = 0
g_problem_size = sys.maxsize

g_validate = True


import math


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


def validate(n_stalls, n_people, max_d, min_d):
    if not g_validate:
        return

    if max_d < min_d:
        error("too much min ")

    if max_d > min_d + 1:
        error("too much max ")


    print([max_d, min_d, pow(2, math.log2(n_stalls) - math.log2(n_people)) / 2])
    # if pow(2, math.log2(n_stalls) - math.log2(n_people)) / 2 < max_d:
    #     error("too max {}".format(max_d, min_d, pow(2, math.log2(n_stalls) - math.log2(n_people)) / 2))

    # if max_d > 2 * min_d:
    #     error("too large {}".format([max_d, min_d]))

### start


from sortedcontainers import SortedDict


def add_count(dict, key, count):
    if key <= 0:
        return

    if key in dict:
        dict[key] = dict[key] + count
    else:
        dict[key] = count


def stalls(n_stalls, n_people):
    # depth = int(math.log(n_people, 2))

    stall_counts = SortedDict()

    add_count(stall_counts, n_stalls, 1)

    n_p = n_people

    while n_p > 0:

        if len(stall_counts) <= 0:
            error("0")
            return 0, 0

        # print("{}\t{}".format(n_p, stall_counts))

        n_s, count = stall_counts.popitem()

        n_p -= count

        min_d = (n_s - 1) // 2
        max_d = (n_s - 1) - min_d

        if n_p <= 0:
            # if n_p < 0:
            #     error(n_p)
            return max_d, min_d
        add_count(stall_counts, min_d, count)
        add_count(stall_counts, max_d, count)

    # n_p = 1
    #
    # while (n_p < n_people/2):
    #     n_p *= 2
    #
    # min_p = (n_people - 1) // 2
    # max_p = (n_people - 1) - min_p
    #
    # # max_d_x = max_d
    # # max_d_n = max_d
    # min_d_x = min_d
    # # min_d_n = min_d
    # if max_d > 0 and max_p > 0:
    #     max_d, min_d_x = stalls(max_d, max_p)
    #     min_d_x = min(min_d, min_d_x)
    # else:
    #     error("")
    #
    # if min_p <= 0:
    #     max_d = max(max_d, min_d)
    #     min_d = min(min_d_x, min_d)
    # elif min_d > 0:
    #     max_d_n, min_d_n = stalls(min_d, min_p)
    #     max_d = max(max_d, max_d_n)
    #     min_d = min(min_d, min_d_n)
    #
    # return max_d, min_d


def assign_stall(n_stalls, n_people):

    return stalls(n_stalls, n_people)

### end


def solve(problem):

    n_stalls, n_people = problem.split(' ')

    max_d, min_d = assign_stall(int(n_stalls), int(n_people))

    validate(int(n_stalls), int(n_people), max_d, min_d)

    return "{} {}".format(max_d, min_d)

f_out = open(g_file_out, 'w')

def run():
    with open(g_file_in) as f_in:
        num_problems = int(f_in.readline())
        i_line = 0
        for line in f_in:
            i_line += 1
            if i_line < g_problem_start:
                continue
            if i_line >= g_problem_start + g_problem_size:
                break

            if line[-1] == '\n':
                line = line[:-1]
            problem = line

            print(i_line)

            result = solve(problem)
            f_out.write("Case #{}: {}".format(i_line, result))
            f_out.write('\n')


run()

f_out.close()
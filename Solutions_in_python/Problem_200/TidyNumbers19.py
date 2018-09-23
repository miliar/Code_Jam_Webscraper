
import time

g_round = ""
g_question = "B"
# g_step = "sample"
# g_step = "small-attempt0"
g_step = "large"

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

    if int(problem) < int(result):
        error("error {} ".format([problem, result]))

    if len(problem) < len(result) or (len(problem) == len(result) and int(problem[0]) < int(result[0])):
        error("error {} ".format([problem, result]))

    last_n = 0
    for i, c in enumerate(result):
        if int(c) < last_n:
            error([result, i, c, last_n])
        last_n = int(c)


import re


def downOneTidy(number):
    if number == '0':
        error("")
    if len(number) == 1:
        return str(int(number) - 1)
    if len(number) > 1:
        pos = number.index(number[-1])
        if pos == 0:
            return str(int(number[-1]) - 1) + '9' * (len(number) - pos - 1)
        elif pos == len(number) - 1:
            return number[0:pos] + str(int(number[-1]) - 1)
        else:
            return number[0:pos] + str(int(number[-1]) - 1) + '9' * (len(number) - pos - 1)


def tidy(number):
    output = ""
    # print("tidy " + number)

    last_n = 0
    for i, c in enumerate(number):
        if int(c) >= last_n:
            output = output + c
            last_n = int(c)
        else:
            if re.search('^1+$', output):
                head = '9' * (len(output) - 1)
            else:
                head = downOneTidy(output)

            n_leftovers = (len(number) - i)

            output = head + ('9' * n_leftovers)
            if len(output) > 1 and output[0] == '0':
                output = output[1:]
            if n_leftovers < 0:
                error(n_leftovers)
            break
    return output


def solve(problem):
    number = problem

    output = tidy(number)

    validate(problem, output)

    return output

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
            result = solve(problem)
            f_out.write("Case #{}: {}".format(i_line, result))
            f_out.write('\n')


run()

f_out.close()
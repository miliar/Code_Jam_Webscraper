__author__ = 'Roberto'
import os
import math

IMPOSSIBLE = "IMPOSSIBLE"

def finish(index, solution):

    print solution

    file_out.write("Case #{0}: {1}\n".format(index+1, solution))

def solve_case(index, test_case):

    print "Case: [{0}]".format(test_case)

    S, K = test_case.split()
    K = int(K)

    pancakes = [p == '+' for p in S]

    solve_rec(index, pancakes, K, 0)

def solve_rec(index, pancakes, K, flips):

    while len(pancakes) > 0:

        if all(pancakes):
            finish(index, flips)
            return

        if len(pancakes) < K:
            finish(index, IMPOSSIBLE)
            return

        if len(pancakes) == K:
            if not any(pancakes):
                finish(index, flips + 1)
                return
            finish(index, IMPOSSIBLE)
            return

        if pancakes[0]:
            i = 0
            while i < len(pancakes) and pancakes[i]:
                i += 1

            pancakes = pancakes[i:]
            continue

        for i in xrange(K):
            pancakes[i] = not pancakes[i]
        flips += 1

    finish(index, flips)


if __name__ == "__main__":

    task = "A"
    level = 2
    attempts = 0

    if level == 0:
        file_name = "sample.in"
    elif level == 1:
        file_name = "{0}-small-attempt{1}.in".format(task, attempts)
    else:
        file_name = "{0}-large.in".format(task)


    file_path = os.path.join(r".", file_name)
    file_out_name = file_path.replace("in", "out")
    file_out = open(file_out_name, 'w')

    with open(file_path, 'r') as file:
        content = file.read()

    lines = content.split('\n')
    number_of_lines = int(lines[0])

    test_cases = lines[1:]

    for i in xrange(0, number_of_lines):

        solve_case(i, test_cases[i])

    file_out.close()
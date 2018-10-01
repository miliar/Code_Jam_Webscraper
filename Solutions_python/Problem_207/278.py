__author__ = 'Roberto'
import math

def finish(index, solution):

    print(solution)

    file_out.write("Case #{0}: {1}\n".format(index+1, solution))
    debug_out.write("{0}\n".format( solution))

def compatible(a, b):

    if b == "ALL":
        return True

    if a == "R":
        return b == "Y" or b == "G" or b == "B"
    if a == "Y":
        return b == "R" or b == "B" or b == "V"
    if a == "B":
        return b == "Y" or b == "R" or b == "O"
    if a == "O":
        return b == "B"
    if a == "V":
        return b == "Y"
    if a == "G":
        return b == "R"

def backtracking(r, o, y, g, b, v, prev):

    if any(num < 0 for num in (r, o, y, g, b, v)):
        return None

    if all(num == 0 for num in (r, o, y, g, b, v)):
        if compatible(prev[0], prev[-1]):
            return prev
        else:
            return None

    if len(prev) == 0:
        last = "ALL"
    else:
        last = prev[-1]

    offsets = {
        "R": [1, 0, 0, 0, 0, 0],
        "O": [0, 1, 0, 0, 0, 0],
        "Y": [0, 0, 1, 0, 0, 0],
        "G": [0, 0, 0, 1, 0, 0],
        "B": [0, 0, 0, 0, 1, 0],
        "V": [0, 0, 0, 0, 0, 1]
    }

    options_map = {
        "ALL": {"Y": y, "G": g, "B": b, "R": r, "V": v, "O": o},
        "R": {"Y": y, "G": g, "B": b},
        "Y": {"B": b, "R": r, "V": v},
        "B": {"R": r, "Y": y, "O": o},
        "O": {"B": b},
        "V": {"Y": y},
        "G": {"R": r}
    }

    options = options_map[last]
    options = sorted([option for option in options if options[option] > 0], key=lambda k: options[k])

    for next in reversed(options):

        temp_prev = prev[:]
        temp_prev.append(next)

        dr, do, dy, dg, db, dv = offsets[next]
        result = backtracking(r - dr, o - do, y - dy, g - dg, b - db, v - dv, temp_prev)
        if result is not None:
            return result

def solve_test(index, test_case):

    debug_out.write("Case #{0} In: {1} Out: ".format(index, test_case))

    print("Case: [{0}]".format(test_case))

    n, r, o, y, g, b, v = map(int, test_case.split())
    if r > y + g + b or b > y + o + r or y > r + v + b:
        finish(index, "IMPOSSIBLE")
        return

    if g > r or o > g or v > y:
        finish(index, "IMPOSSIBLE")
        return

    result = backtracking(r, o, y, g, b, v, [])
    if result is None:
        finish(index, "IMPOSSIBLE")
    else:
        finish(index, "".join(result))

if __name__ == "__main__":

    import sys
    sys.setrecursionlimit(1500)
    # generate tests
    if False:
        import random
        print(100)
        for i in range(100):
            colors = [0, 0, 0, 0, 0, 0]
            for j in range(1000):
                i = random.choice(range(6))
                colors[i] += 1
            print(1000, end=" ")
            print(" ".join(map(str, colors)))

        exit()

    task = "B"
    level = 1
    attempts = 1

    if level == 0:
        file_name = "sample.in"
    elif level == 1:
        file_name = "{0}-small-attempt{1}.in".format(task, attempts)
    else:
        file_name = "{0}-large.in".format(task)



    file_out_name = file_name.replace("in", "out")
    file_out = open(file_out_name, 'w')
    debug_out = open(file_name.replace("in", "debug"), 'w')

    with open(file_name, 'r') as file:
        content = file.read()

    lines = content.split('\n')
    number_of_lines = int(lines[0])

    test_cases = lines[1:]

    for i in range(0, number_of_lines):

        solve_test(i, test_cases[i])

    file_out.close()
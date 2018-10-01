import argparse
import shutil
import math

parser = argparse.ArgumentParser()
parser.add_argument('problem',  help='Problem name')
parser.add_argument('suffix',  help='Type')
args = parser.parse_args()

problem_name = args.problem
problem_type = args.suffix

input_path = "{}-{}.in".format(problem_name, problem_type)
output_path = "{}-{}.out".format(problem_name, problem_type)
code_path = "{}.py".format(problem_name)

with open(input_path, 'r') as in_file, open(output_path, 'w') as out_file:
    cases = int(in_file.readline().strip())

    for c in range(cases):
        def parse_case():
            def line():
                return in_file.readline().strip()

            def tokens():
                return line().split(" ")

            def ints():
                return map(int, tokens())

            # Read case input

            return line()

        def output(res):
            case_solution = 'Case #{}: {}'.format(c+1, res)
            out_file.write(case_solution)
            out_file.write('\n')
            print(case_solution)

        num = parse_case()

        def solve(n):
            i = 0
            incr = 0
            while i < len(n) - 1:
                if n[i] < n[i + 1]:
                    incr = i + 1
                elif n[i] > n[i + 1]:
                    r = pow(10, len(n) - incr - 1)
                    return int(math.floor(float(n) / r)) * r - 1

                i += 1

            return int(n)

        output((solve(num)))

shutil.copyfile('gcj.py', code_path)

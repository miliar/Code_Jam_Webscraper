from sys import argv, exit
import numpy as np

def get_input(inputfile):

    def read_int():
        return int(inputfile.readline().strip())
    def read_ints():
        return np.array(inputfile.readline().split(), dtype=int)
    def read_bigints(): #For ints that won't fit directly in an int32 array
        line = inputfile.readline().split()
        return np.array(map(lambda x: int(x), line))
    def read_float():
        return float(inputfile.readline().strip())
    def read_floats():
        return np.array(inputfile.readline().split(), dtype=float)
    def read_string():
        return inputfile.readline().strip()
    def read_strings():
        return np.array(inputfile.readline().split(), dtype=object)
    
    abc = read_strings()

def solve_problem(a, b, c):

    possible_nums = {}
    high = max(a, b)
    low = min(a, b)

    for num1 in range(high):
        for num2 in range(low):
            
            if possible_nums.get(num1&num2):
                possible_nums[num1&num2] += 1
            else:
                possible_nums[num1&num2] = 1
    

    combinations = 0
    for i in range(c):
        if possible_nums.get(i):
            combinations += possible_nums[i]

    return combinations

if __name__ == "__main__":

    cmd_args = argv[1:]
    inputfile = ""

    if not len(cmd_args) or len(cmd_args) > 2:
        print("Invalid number of args! Exiting")
        exit(1)

    if not cmd_args[0].endswith(".in"):
        print("Invalid inputfile! Exiting")
        exit(1)

    input_filename = cmd_args[0]
    output_filename = input_filename[:-3] + "_out.out"

    inputfile = open(input_filename, "r")
    outputfile = open(output_filename, "w+")
    print("Created file: {}\n".format(output_filename))

    num_cases = int(inputfile.readline().strip())
    
    # solve the cases one-by-one
    for case in range(num_cases):
        input_line = inputfile.readline().split()

        a = int(input_line[0])
        b = int(input_line[1])
        k = int(input_line[2])

        solution_str = solve_problem(a, b, k)

        outputfile.write("Case #{0:}: {1:}\n".format(case+1, solution_str))
        print(("Case #{0:}: {1:}\n".format(case+1, solution_str)))

    inputfile.close()
    outputfile.close()

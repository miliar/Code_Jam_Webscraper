import sys
import math
    
def print_ans(case_num,solution):
    print("Case #"+str(case_num)+":"),
    print_solution(solution)

def print_solution(solution):
    """TO DO"""
    print solution


def input_processor(filename):
    f=open(filename)
    data=f.read().split("\n")
    case_nums=int(data[0])

    """Insert number of lines per test case here"""
    num_of_lines=1
    data_length=len(data)

    """Edit start_index here"""
    start_index=1
    case_num=1
    
    for i in xrange(0,case_nums):
        start=(i*num_of_lines)+start_index
        problem=data[start:start+num_of_lines]
        process_input_case(case_num,problem)
        case_num+=1

def process_input_case(case_num,problem):
    """Process raw input into apropriate type"""
    problem_variable = int(problem[0])
    solve(case_num,problem_variable)

def solve(case_num,problem_variable):
    strdigits = str(problem_variable)
    digits = len(strdigits)
    temp = problem_variable
    for i in xrange(digits-1):
        if int(strdigits[-(i+1)])< int(strdigits[-(i+2)]):
            divider = int(math.pow(10, i+1))
            temp = (temp / divider) * divider - divider + int("9"*(i+1))
            strdigits = str(temp)
        

    print_ans(case_num, temp)

def main():
    input_file=sys.argv[1]
    input_processor(input_file)


if __name__=="__main__":
    main()

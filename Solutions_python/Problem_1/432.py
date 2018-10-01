from helper_functions import *


def solve_problem(input, output):
    n_cases = getnum(input)
    for case in range(n_cases):
        n_names = getnum(input)
        names = set()
        for n in range(n_names):
            names.add(getline(input))
        
        n_queries = getnum(input)
        queries = [getline(input) for n in range(n_queries)]
        
        path_length = get_path_length(queries, names)
        
        answer(path_length, output)

def get_path_length(queries, names):
    n_swallowed = 0
    for name in names:
        try:
            n_swallowed = max(n_swallowed, queries.index(name))
        except ValueError:
            return 0 #no need for any changes: we have a name which doesn't conflict
    
    return 1 + get_path_length(queries[n_swallowed:], names)
    
    
    

if __name__ == "__main__":
    test_input = """2
5
Yeehaw
NSM
Dont Ask
B9
Googol
10
Yeehaw
Yeehaw
Googol
B9
Googol
NSM
B9
NSM
Dont Ask
Googol
5
Yeehaw
NSM
Dont Ask
B9
Googol
7
Googol
Dont Ask
NSM
NSM
Yeehaw
Yeehaw
Googol    """
    test_output = """Case #1: 1
Case #2: 0
    """
    
    do_test(solve_problem, test_input, test_output)
    
    do_real(solve_problem)
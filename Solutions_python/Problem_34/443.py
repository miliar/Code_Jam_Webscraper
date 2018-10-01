import re

from helper_functions import *

def solve_problem(input, output):
    L, D, N = getnums(input)
    dictionary = []
    for d in xrange(D):
        word = getline(input)
        dictionary.append(word)
    for n in xrange(N):
        case = getline(input)
        pattern = case.replace('(', '[').replace(')', ']')
        reg = re.compile(pattern)
        count = len([word for word in dictionary if re.match(pattern, word)])
        answer(count, output)


if __name__ == "__main__":
    test_input = """
3 5 4
abc
bca
dac
dbc
cba
(ab)(bc)(ca)
abc
(abc)(abc)(abc)
(zyx)bc
    """
    test_output = """
Case #1: 2
Case #2: 1
Case #3: 3
Case #4: 0
    """
    
    do_test(solve_problem, test_input, test_output)
    
    do_real(solve_problem)
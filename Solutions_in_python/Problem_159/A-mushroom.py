from codejam import *

def read_file(f):
    num = read_int(f)
    lst = read_int_list(f)
    return (num, lst)

def solver(case):
    num, lst = case
    difference = tuple((lst[i]-lst[i+1] for i in range(num-1)))
    ans1 = sum(filter(lambda x: x > 0, difference))
    max_diff = max(difference)
    ans2 = sum(map(lambda x: min(x, max_diff), lst[:-1]))
    return str(ans1) + ' ' + str(ans2)

solve('A-large', read_file, solver)

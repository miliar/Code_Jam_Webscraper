from helper_functions import *
from operator import iadd

def solve_problem(input, output):
    n_cases = getnum(input)
    for case in range(n_cases):
        solve_case(input, output)
        
def solve_case(input, output):
    T = getnum(input)
    NA, NB = map(int, getwords(input))
    
    # each action takes the form (time, a_trains, b_trains)
    # where a_trains is the change in available trains at a. 
    # (leaving positive sign convention ensures correct sorting) 
    all_actions = [] 
    for n in range(NA):
        t_depart, t_arrive = get_times(input)
        t_availible = t_arrive + T
        all_actions.append((t_depart, 1, 0))
        all_actions.append((t_availible, 0, -1))
    for n in range(NB):
        t_depart, t_arrive = get_times(input)
        t_availible = t_arrive + T
        all_actions.append((t_depart, 0, 1))
        all_actions.append((t_availible, -1, 0))
    
    # NOTE: the sign convention ensures that a train can become 
    # available and leave in the same minute.
    all_actions.sort()
    
    # should be positive most of the time
    deficit_at_a = 0
    deficit_at_b = 0
    
    # Should end up as max(deficit_at_a)
    max_deficit_at_a = 0
    max_deficit_at_b = 0
    
    # Simulate the day's trains, and record the worst deficit.
    for time, a_needed, b_needed in all_actions:
        deficit_at_a += a_needed
        deficit_at_b += b_needed
        
        max_deficit_at_a = max(max_deficit_at_a, deficit_at_a)
        max_deficit_at_b = max(max_deficit_at_b, deficit_at_b)
    
    result = (max_deficit_at_a, max_deficit_at_b)
    answer(result, output)


def get_times(input):
    """times as integers (minutes since 00:00)"""
    stringa, stringb = getwords(input)
    #sorry: a bit obtuse. Makes me look like a perl hacker or something:
    hour_a, minute_a = map(int, stringa.split(':'))
    hour_b, minute_b = map(int, stringb.split(':'))
    
    return (60 * hour_a) + minute_a, (60 * hour_b) + minute_b


if __name__ == "__main__":
    test_input = """
3
5
3 2
09:00 12:00
10:00 13:00
11:00 12:30
12:02 15:00
09:00 10:30
2
2 0
09:00 09:01
12:00 12:02
0
1 1
09:00 09:01
09:01 12:02
    """
    test_output = """
Case #1: 2 2
Case #2: 2 0
Case #3: 1 0
    """
    
    do_test(solve_problem, test_input, test_output)
    
    do_real(solve_problem)
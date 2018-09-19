'''
Qualification Round 2014, B - Cookie Clikcer Alpha
'''

import sys

def read_test_case(line):

    inputs = [float(n) for n in line.split()]
    return inputs

MIN_TIME = None

def solve_test_case(C, F, X, cookies_per_second = 2,
        number_of_cookies = 0, time_so_far = 0):

    '''
    C - cost to buy a farm
    F - extra cookies per second from farm
    X - number of cookies on the side inorder to win
    '''
    global MIN_TIME

    while True:

        if MIN_TIME != None and time_so_far > MIN_TIME:
            return

        # decide if to wait till get to X  or to buy another farm
        
        # A: wait till get to X cookies
        time_to_get_to_X_by_doing_nothing = X / cookies_per_second
        final_time = time_so_far + time_to_get_to_X_by_doing_nothing

        # add final time to list
        if MIN_TIME is None:
            MIN_TIME = final_time
        if final_time < MIN_TIME:
            MIN_TIME = final_time

        # B: or buy a farm
        # calc the time to buy a farm and the params in it, and if it's
        # bigger than the min, don't continue
        time_to_buy_a_farm = C / cookies_per_second

        cookies_per_second += F
        time_so_far += time_to_buy_a_farm

def main():

    input_path = sys.argv[1]
    output_path = sys.argv[1].replace('.in', '.out')
    input_lines = open(input_path, 'rb').readlines()
    output_file = open(output_path, 'w')
    
    number_of_cases = int(input_lines[0])
    for i in xrange(number_of_cases):

        C, F, X = read_test_case(input_lines[i + 1])
        global MIN_TIME
        MIN_TIME = None
        print i + 1, ':  ', input_lines[i + 1]
        solve_test_case(C,F,X)
        print MIN_TIME

        output_file.write("Case #%d: %.7f\n" % (i + 1, MIN_TIME))

if __name__=='__main__':
    main()

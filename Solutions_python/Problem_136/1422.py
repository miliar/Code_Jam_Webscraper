import sys
import re

def parse_input(input_file, output_file):
    num_test_cases = -1
    test_num = 1
    with open(input_file, 'r') as f_in:
        with open(output_file, 'w') as f_out:
            for line in f_in:
                if num_test_cases == -1:
                    num_test_cases = int(line)
                else:
                    num_list = re.findall(r'[0-9.]+', line)
                    num_list = list(float(val) for val in num_list)
                    c, f, x = num_list
                    result = compute_time(c, f, x)
                    write_output(f_out, test_num, result)
                    test_num += 1

def write_output(file_handle, test_num, value):
    file_handle.write("Case #" + str(test_num) + ": " + str(value) + "\n")
    print("Wrote output for test case: " + str(test_num))

def compute_time(c, f, x):
    curr_rate = 2
    elapsed_time = 0.0
    while True:
        no_factory_time = x/curr_rate
        time_to_next_factory, new_rate = c/curr_rate, curr_rate + f
        new_factory_time = time_to_next_factory + x/new_rate
        if new_factory_time < no_factory_time:  # Build new factory.
            elapsed_time += time_to_next_factory
            curr_rate = new_rate
        else:
            elapsed_time += no_factory_time
            return elapsed_time

if __name__=='__main__':
    if len(sys.argv) == 2:
        input_file = sys.argv[1]
        output_file = "cookie_clicker.out"
        parse_input(input_file, output_file)
    elif len(sys.argv) == 3:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        parse_input(input_file, output_file)
    else:
        print("Incorrect number of arguments supplied: " + str(len(sys.argv)))
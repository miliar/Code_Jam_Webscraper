#!/usr/bin/env python

import sys, os

def parse_list(line):
    # Ignore the first token, its just the number of button presses
    tokens = line.split(' ')[1:]
    return tokens

def calculate_seconds(tokens):
    is_o = (lambda x: x == 'O')
    is_b = (lambda x: x == 'B')
    o_buttons, b_buttons = [], []
    count = 1
    for i in xrange(0, len(tokens), 2):
        if is_o(tokens[i]):
            o_buttons.append((count, int(tokens[i+1])))
        else:
            b_buttons.append((count, int(tokens[i+1])))
        count += 1

    get_count = (lambda x: x[0])
    get_position = (lambda x: x[1])

    o_pos, b_pos = 1, 1
    seconds = 0
    while o_buttons or b_buttons:
        if o_buttons and b_buttons:
            b_count = get_count(b_buttons[0])
            b_target = get_position(b_buttons[0])
            o_count = get_count(o_buttons[0])
            o_target = get_position(o_buttons[0])
            if b_count < o_count:
                b_moves = abs(b_target - b_pos)
                b_seconds = b_moves + 1
                b_pos = b_target
                seconds += b_seconds
                o_moves = o_target - o_pos
                if o_moves:
                    if abs(o_moves) <= b_seconds:
                        o_pos = o_target
                    else:
                        o_pos = o_pos + (o_moves / abs(o_moves)) * b_seconds
                b_buttons.pop(0)
            else:
                o_moves = abs(o_target - o_pos)
                o_seconds = o_moves + 1
                o_pos = o_target
                seconds += o_seconds
                b_moves = b_target - b_pos
                if b_moves:
                    if abs(b_moves) <= o_seconds:
                        b_pos = b_target
                    else:
                        b_pos = b_pos + (b_moves / abs(b_moves)) * o_seconds
                o_buttons.pop(0)
        elif o_buttons:
            o_target = get_position(o_buttons[0])
            o_moves = abs(o_target - o_pos)
            o_seconds = o_moves + 1
            o_pos = o_target
            seconds += o_seconds
            o_buttons.pop(0)
        else:
            b_target = get_position(b_buttons[0])
            b_moves = abs(b_target - b_pos)
            b_seconds = b_moves + 1
            b_pos = b_target
            seconds += b_seconds
            b_buttons.pop(0)
    return seconds

if __name__ == '__main__':
    dir_name = os.path.dirname(os.path.abspath(__file__))
    if len(sys.argv) == 2:
        # input file is specified
        input_file = open(sys.argv[1])
    else:
        input_file = open(dir_name + '/test_input.txt')
    output = []
    count = 0
    for line in input_file:
        line = line.strip('\n')
        if count == 0:
            num_tests = int(line)
        elif line:
            button_list = parse_list(line)
            test_output = calculate_seconds(button_list)
            output.append("Case #{0}: {1}".format(count, test_output))
        count += 1
    assert len(output) == num_tests, "Invalid number of test case output lines"
    for line in output:
        print(line)

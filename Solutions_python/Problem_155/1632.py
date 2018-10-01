#!/usr/bin/env python

def read_stdin_lines():
    import fileinput
    return [line for line in fileinput.input()]

def parse_lines(lines):
    num_test_cases = int(lines.pop(0))
    return [[int(c) for c in list(line.split()[1])] for line in lines]

def solve(inputs):
    cum_sum = 0
    diff = 0
    for target, n in enumerate(inputs):
        if cum_sum + diff < target:
            diff += (target - cum_sum - diff)
        cum_sum += n
    return diff

def print_outputs(outputs):
    for n, output in enumerate(outputs):
        print "Case #{}: {}".format(n+1, output)

if __name__ == '__main__':
    lines = read_stdin_lines()
    inputs = parse_lines(lines)
    outputs = map(solve, inputs)
    print_outputs(outputs)

""" Pancake Flipping Problem again"""

from sys import stdin

def flip_cakes(stack, start_pos, length):
    """ Helper function for performing a single flip"""
    if start_pos + length > len(stack):
        return False, stack
    else:
        new_stack = ""
        for i in range(len(stack)):
            if i >= start_pos and i < start_pos+length:
                if stack[i] == '-':
                    new_stack += '+'
                else:
                    new_stack += '-'
            else:
                new_stack += stack[i]
        return True, new_stack


def solve_flipping(stack, length):
    """ The basic idea is that since we cannot flip off the edge of the stack,
    we can iteratively flip the bottom of the stack to the top. If we cannot
    successfully flip the end of the stack, then it is impossible. """
    flip_counter = 0
    for i in range(len(stack)):
        if stack[i] == '-':
            valid, stack = flip_cakes(stack, i, length)
            if not valid:
                return -1
            flip_counter += 1

    return flip_counter

def main():
    test_cases  = int(stdin.readline())
    for i in range(1, test_cases + 1):
        line = stdin.readline().split()
        stack = line[0]
        flipper_length = int(line[1])
        flip_counter = solve_flipping(stack, flipper_length)
        if flip_counter < 0:
            print("Case #%s: IMPOSSIBLE" % str(i))
        else:
            print("Case #%s: %s" % (str(i), str(flip_counter)))

main()

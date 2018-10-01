#!/usr/bin/env python

import sys, os

def parse(line):
    combos, opposed = [], []
    tokens = line.split(' ')
    index = 0
    combo_num = int(tokens[index])
    if combo_num:
        for i in xrange(1, combo_num+1):
            combos.append(tokens[index+i])
        index += combo_num + 1
    else:
        index += 1
    opposed_num = int(tokens[index])
    if opposed_num:
        for i in xrange(1, opposed_num+1):
            opposed.append(tokens[index+i])
        index += opposed_num + 1
    else:
        index += 1
    invoked = list(tokens[index+1])
    return combos, opposed, invoked

def calculate_magick(combos, opposed, invoked):
    combo_lookup = {}
    for combo in combos:
        combo_str = combo[:2]
        combo_lookup[combo_str] = combo[2]
        combo_lookup[combo_str[::-1]] = combo[2]
    opposed_lookup = {}
    for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        opposed_lookup.setdefault(letter, set())
    for oppose in opposed:
        opposed_lookup[oppose[0]].add(oppose[1])
        opposed_lookup[oppose[1]].add(oppose[0])
    magick = []
    for letter in invoked:
        magick.append(letter)
        if len(magick) > 1:
            end_letters = ''.join(magick[-2:])
            if end_letters in combo_lookup:
                magick = magick[:-2]
                magick.append(combo_lookup[end_letters])
        letter = magick[-1]
        if set(magick[:-1]) & opposed_lookup[letter]:
            magick = []
    return magick

def format_magick(magick):
    return '[' + ', '.join(magick) + ']'

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
            combos, opposed, invoked = parse(line)
            magick = calculate_magick(combos, opposed, invoked)
            output.append("Case #{0}: {1}".format(count, format_magick(magick)))
        count += 1
    assert len(output) == num_tests, "Invalid number of test case output lines"
    for line in output:
        print(line)

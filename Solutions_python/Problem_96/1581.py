#! /usr/bin/env python

import sys

# For each total, what is the high score
regular_scores = dict()
surprising_scores = dict()
for score in range(0, 11):
    regular_scores[score * 3] = score
    regular_scores[score * 3 + 1] = score + 1
    regular_scores[score * 3 + 2] = score + 1

    # Special
    surprising_scores[score * 3 + 2] = score + 2
    surprising_scores[score * 3 + 3] = score + 2
    surprising_scores[score * 3 + 4] = score + 2

input_file = open(sys.argv[1], 'r')
output_file = open(sys.argv[1].replace(".in", ".out"), 'w')
for num, row in enumerate(input_file):
    if num == 0:
        continue

    numbers = [int(x) for x in row.split(' ')]

    regular_count = 0
    surprising_count = 0
    
    for score in numbers[3:]:
        if regular_scores[score] >= numbers[2]:
            regular_count += 1
        elif score > 2 and surprising_scores[score] >= numbers[2]:
            surprising_count += 1

    total_count = regular_count
    if surprising_count > numbers[1]:
        total_count += numbers[1]
    else:
        total_count += surprising_count

    output_file.write("Case #{0}: {1}\n".format(num, total_count))

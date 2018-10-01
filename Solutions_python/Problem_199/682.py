#!/usr/bin/python3
from __future__ import print_function
import sys

#~ debug = True
debug = False


def detectImpossible(pancakes, flipper):
    if len(pancakes) < 2 * flipper:
        pancakeAlwaysTogether = pancakes[len(pancakes) - flipper:flipper]
        if '+' in pancakeAlwaysTogether and '-' in pancakeAlwaysTogether:
            return True
    return False


def flipPancakes(pancakes, flipper, position):
    if position + flipper > len(pancakes):
        return False, []
    partFlipped = pancakes[position:position + flipper]
    partFlipped = ['-' if p == '+' else '+' for p in partFlipped]
    return True, pancakes[:position] + ''.join(partFlipped) + pancakes[position + flipper:]


def getFlips(pancakes, flipper):
    flippedPancakes = pancakes
    steps = 0
    while '-' in flippedPancakes:
        position = flippedPancakes.index('-')
        possible, flippedPancakes = flipPancakes(flippedPancakes, flipper, position)
        if not possible:
            return False, []
        if debug: print(flippedPancakes)
        steps += 1
    return True, steps


lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

n = int(lines[0])
for i in range(n):
    pancakes, flipper = lines[i+1].split(' ')
    flipper = int(flipper)
    if debug: print('#' * 20)
    if debug: print(pancakes, flipper)

    if detectImpossible(pancakes, flipper):
        print('Case #' + str(i+1) + ': IMPOSSIBLE')
    else:
        if '-' not in pancakes:
            print('Case #' + str(i+1) + ': 0')
        else:
            possible, flips = getFlips(pancakes, flipper)
            if possible:
                print('Case #' + str(i+1) + ': ' + str(flips))
            else:
                print('Case #' + str(i+1) + ': IMPOSSIBLE')

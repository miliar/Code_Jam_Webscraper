#!/usr/bin/env python

from StringIO import StringIO
import sys

INPUT = '''3
4 O 2 B 1 B 2 O 4
3 O 5 O 8 B 100
2 B 2 B 1
'''

OUTPUT = '''Case #1: 6
Case #2: 100
Case #3: 4
'''

def parse_pairs(line):
    components = line.split()

    orange = []
    blue = []

    n = int(components.pop(0))
    for i in range(n):
        color = components.pop(0)
        number = int(components.pop(0))
        if color == 'O':
            orange.append((i, number))
        else:
            blue.append((i, number))

    return orange, blue

def direction(f, t):
    n = (t-f)
    if n:
        return n/abs(n)
    else:
        return 0

def get_next(list):
    return list.pop(0) if list else (sys.maxint, None)

def calculate_moves(orange, blue):
    '''Keep orange and blue always moving toward their target, but syncronize the order the buttons
    are pressed'''

    orange = orange[:]
    blue = blue[:]

    blue_position = 1
    orange_position = 1

    count = 0

    orange_order, orange_target_position = get_next(orange)
    blue_order, blue_target_position = get_next(blue)

    # 0 isn't a valid position, so this comparison is okay
    while orange_target_position or blue_target_position:
        orange_can_push = True

        if blue_target_position == blue_position and blue_order < orange_order:
            # Push
            blue_order, blue_target_position = get_next(blue)
            orange_can_push = False
        elif blue_target_position:
            # Move
            blue_position += direction(blue_position, blue_target_position)

        if orange_target_position == orange_position and orange_order < blue_order and orange_can_push:
            # Push
            orange_order, orange_target_position = get_next(orange)
        elif orange_target_position:
            # Move
            orange_position += direction(orange_position, orange_target_position)
        
        count += 1
    
    return count

def main(stdin, stdout):
    stdin.next()  # Skip the first line
    for i, line in enumerate(stdin, 1):
        orange, blue = parse_pairs(line)
        moves = calculate_moves(orange, blue)
        stdout.write('Case #{0}: {1}\n'.format(i, moves))

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'test':
        output = StringIO()
        main(StringIO(INPUT), output)
        output.seek(0)
        output = output.read()
        assert output == OUTPUT, '{0} != {1}'.format(output, OUTPUT)
        print "OK"
    else:
        main(sys.stdin, sys.stdout)

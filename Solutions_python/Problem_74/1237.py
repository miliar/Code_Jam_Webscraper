import sys

def read_test_case():
    line = sys.stdin.readline().split()
    for button in xrange(int(line[0])):
        yield (line[2 * button + 1], int(line[2 * button + 2]))

def read_test_cases():
    for case in xrange(int(sys.stdin.readline())):
        yield read_test_case()

def other(color):
    if 'O' == color:
        return 'B'
    return 'O'

def solve_case(case):
    push_time = {}
    push_position = {}
    push_time['O'] = 0
    push_time['B'] = 0
    push_position['O'] = 1
    push_position['B'] = 1
    for (color, position) in case:
        push_time[color] = max(
            push_time[color] + abs(position - push_position[color]) + 1,
            push_time[other(color)] + 1)
        push_position[color] = position
        #print 'Push %s at position %d at time %d' % \
        #3    (color, position, push_time[color])
    return max(push_time['O'], push_time['B'])

def print_cases():
    i = 1
    for case in read_test_cases():
        print 'Case #%d: %d' % (i, solve_case(case))
        i += 1

print_cases()
        

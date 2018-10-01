import sys, itertools

lines_per_case = 1

other = {'B': 'O', 'O': 'B'}


def solve_case(case):
    actions = case[0].split()[1:]
    actions = itertools.izip(actions[::2], actions[1::2])
    last = {'O': {'b':1, 't': 0}, 'B': {'b':1, 't': 0}}

    current = next(actions)
    last_bot = current[0]
    total = t = get_time(last_bot, current[1], last)

    last[last_bot]['t'] = t
    last[last_bot]['b'] = current[1]


    for action in actions:
        bot = action[0]
        ot = 0
        if last_bot != bot:
            last[bot]['t'] = 0
            last_bot = bot
            ot = last[other[bot]]['t']
        t = get_time(last_bot, action[1], last)
        efft = t - ot if t > ot else 1
        total += efft
        last[last_bot]['t'] += efft
        last[last_bot]['b'] = action[1]

    return str(total)


def get_time(bot, button, state):
    return abs(int(button) - int(state[bot]['b'])) + 1


def produce_output(index, solution):
    print 'Case #%s: %s' % (index, solution)


def get_test_cases(lines, n_of_lines_per_case=1):
    return itertools.izip(*(iter(lines[i::n_of_lines_per_case] for i in range(n_of_lines_per_case))));

if __name__ == "__main__":
    if(len(sys.argv) > 1):
        fn = sys.argv[1]
        with open(fn) as f:
            lines = f.readlines()
            nt = int(lines[0])
            for index, case in enumerate(get_test_cases(lines[1:], lines_per_case), 1):
                solution = solve_case(case)
                produce_output(index, solution)
            

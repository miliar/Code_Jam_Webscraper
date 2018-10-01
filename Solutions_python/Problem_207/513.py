def get_unicorns_placement_small(N, R, Y, B):
    unicorns_count = {'R': R, 'Y': Y, 'B': B}
    if unicorns_count['R'] > 0:
        placement = 'R'
        unicorns_count['R'] -= 1
    elif unicorns_count['Y'] > 0:
        unicorns_count.pop('R')
        placement = 'Y'
        unicorns_count['Y'] -= 1
    elif unicorns_count['B'] > 0:
        unicorns_count.pop('R')
        unicorns_count.pop('Y')
        placement = 'B'
        unicorns_count['B'] -= 1
    else:
        return 'IMPOSSIBLE'
    colors = list(unicorns_count.keys())
    for key in colors:
        if unicorns_count[key] == 0:
            unicorns_count.pop(key)
    for idx in range(N - 1):
        unicorn_max = None
        if idx == N - 3:
            if len(unicorns_count) < 2:
                return 'IMPOSSIBLE'
            elif placement[0] in unicorns_count.keys() and placement[0] != placement[-1]:
                unicorn_max = placement[0]
        elif idx == N - 2:
            if list(unicorns_count.keys())[0] == placement[0]:
                return 'IMPOSSIBLE'
        if unicorn_max is None:
            unicorn_max_count = -1
            for unicorn, count in unicorns_count.items():
                if unicorn != placement[-1] and count > 0:
                    if count > unicorn_max_count:
                        unicorn_max = unicorn
                        unicorn_max_count = count
        if unicorn_max is None:
            return 'IMPOSSIBLE'
        placement += unicorn_max
        unicorns_count[unicorn_max] -= 1
        if unicorns_count[unicorn_max] == 0:
            unicorns_count.pop(unicorn_max)
    check_placement(placement)
    return placement

def check_placement(placement):
    for idx in range(len(placement)):
        if placement[idx] == placement[idx - 1] or placement[idx] == placement[(idx + 1) % len(placement)]:
            raise AssertionError('Incorrect result: ' + placement)

# print(get_unicorns_placement_small(6, 2, 2, 2))
# print(get_unicorns_placement_small(3, 1, 2, 0))
# print(get_unicorns_placement_small(9, 2, 4, 3))
# print(get_unicorns_placement_small(2, 1, 0, 1))

test_cases = int(input())
for i in range(1, test_cases + 1):
    input_str = input()
    params = input_str.split(' ')
    N = int(params[0])
    R = int(params[1])
    O = int(params[2])
    Y = int(params[3])
    G = int(params[4])
    B = int(params[5])
    V = int(params[6])
    answer = get_unicorns_placement_small(N, R, Y, B)
    print("Case #{}: {}".format(i, answer))

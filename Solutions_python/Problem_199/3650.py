def flip(pancakes, position, flipper_size):
    """
    Given a row of pancakes, flips them given a starting position.
    """
    for i in range(0, flipper_size):
        pancakes[position+i] = '-' if pancakes[position+i] == '+' else '+'

def compute_flips(pancakes, flipper_size):
    pancakes_length = len(pancakes)
    current_position = pancakes_length - flipper_size
    flips = 0

    # Look at the edge of our flipper
    # If it's a -, flip
    # move flipper up
    while current_position >= 0:
        if pancakes[current_position-1+flipper_size] == '-':
            flip(pancakes, current_position, flipper_size)
            flips += 1
        current_position -= 1

    # If we can't fit the flipper anymore, final check.
    if '-' in pancakes:
        return -1
    else:
        return flips

# ---- Marshall input/output
cases = int(raw_input())
for case in range(0,cases):
    case_data = raw_input()
    raw_pancakes, size = case_data.split(' ')

    flips = compute_flips([pancake for pancake in raw_pancakes], int(size))
    flips = flips if flips >= 0 else 'IMPOSSIBLE'
    print 'Case #{}: {}'.format(case+1, flips)

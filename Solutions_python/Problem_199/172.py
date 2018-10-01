
def solve_case(state, k):

    # This is basically like playing 1-d "Lights Out"

    num_flips = 0
    flip_start = 0

    while flip_start < len(state) - k + 1:
        if state[flip_start] == '+':
            flip_start += 1
        elif state[flip_start] == '-':
            num_flips += 1
            for i in range(k):
                current = flip_start + i
                if state[current] == '-':
                    state[current] = '+'
                else:
                    state[current] = '-'
        else:
            print("ERROR: Bad state character!")

    # Look at the last k-1 states
    # If they're all + we're good
    # Otherwise there is a parity error and it's impossible
    possible = True
    for i in range(k - 1):
        if state[-(i + 1)] != '+':
            possible = False
            break

    if possible:
        return num_flips
    else:
        return "IMPOSSIBLE"



num_cases = int(input())

for case in range(num_cases):
    case_string = input()
    state = list(case_string.split(' ')[0])
    k = int(case_string.split(' ')[1])

    result = solve_case(state, k)

    print("Case #" + str(case + 1) + ": " + str(result))

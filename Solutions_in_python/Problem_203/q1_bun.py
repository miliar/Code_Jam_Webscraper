R = 0
C = 0


def main():
    T = int(raw_input().strip())
    global R
    global C
    for case_num in range(T):
        print 'Case #{}:'.format(case_num + 1)
        R, C = map(int, raw_input().strip().split(' '))
        state = [None for r in range(R)]

        for r in range(R):
            row = map(list, raw_input().strip().split(' '))
            state[r] = row[0]
        state = check_col(state)
        state = check_row(state)
        for s in state:
            print ''.join(s)



def check_row(state):
    global R
    global C
    for r in range(R):
        is_first = True
        for c in range(C):
            if state[r][c] != '?' and is_first:
                is_first = False
                for c2 in range(c):
                    state[r][c2] = state[r][c]
            elif state[r][c] == '?' and not is_first:
                state[r][c] = state[r][c-1]
    return state


def check_col(state):
    global R
    global C
    for c in range(C):
        is_first = True
        for r in range(R):
            if state[r][c] != '?' and is_first:
                is_first = False
                for r2 in range(r):
                    state[r2][c] = state[r][c]
            elif state[r][c] == '?' and not is_first:
                state[r][c] = state[r-1][c]
    return state


if __name__ == '__main__':
    main()

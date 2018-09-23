

def is_tidy(N):
    str_N = list(str(N))
    return str_N == sorted(str_N)


def find_largest_tidy(N):
    for i in range(N, 0, -1):
        if is_tidy(i):
            return i


def find_tidy_digit(N, index, start):
    base = int(''.join(['1']*index))
    for i in range(9, start-1, -1):
        if i*base <= N:
            return i


def find_largest_tidy2(N):
    digit_arr = map(int, list(str(N)))
    tidy_digit = 0
    tidy = 0
    for i in range(len(str(N)), 0, -1):
        tidy_digit = find_tidy_digit(N-tidy, i, tidy_digit)
        tidy += tidy_digit*(10**(i-1))
    return tidy


if __name__ == '__main__':
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        N = int(input())
        y = find_largest_tidy2(N)
        print("Case #{}: {}".format(i, y))

    #for i in range(1, 10001):
    #    assert find_largest_tidy(i)== find_largest_tidy2(i)
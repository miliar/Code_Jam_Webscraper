#import pdb

def is_tidy(N):
    prev = 0
    for digit in (int(x) for x in str(N)):
        if digit < prev:
            return False

        prev = digit

    return True


def naive_solve(N):
    for x in range(N, 0, -1):
        if is_tidy(x):
            return x


def make_tail_nines(i, digits):
    for j in range(i, len(digits)):
        digits[j] = 9

def solve(N):
    digits = [int(x) for x in str(N)]

    #if N == 10: pdb.set_trace()

    for _ in range(len(digits)):
        prev = digits[0]
        for i, d in enumerate(digits):
            if d < prev:
                make_tail_nines(i, digits)
                digits[i - 1] -= 1

            prev = d

    return int(''.join(str(x) for x in digits))


def parse_line():
    N = int(input())
    return N

def stress_test():
    import sys
    for N in range(1, 10**18):
        sys.stdout.write('\rTest Case: %d' % (N))
        if naive_solve(N) != solve(N):
            print()
            print('Failed with input', N, 'ans given =', solve(N), 'real answer =', naive_solve(N))
            break

def main():
    T = int(input())

    for case_num in range(1, T+1):
        ans = solve(parse_line())
        print('Case #', case_num, ': ', ans, sep='')



if __name__ == '__main__':
    main()
    #stress_test()
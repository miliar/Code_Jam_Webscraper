def main():
    t = int(raw_input())
    for i in range(t):
        n = int(raw_input())
        last_tidy = solve(n)
        print('Case #{}: {}'.format(i + 1, last_tidy))

def is_tidy(n):
    curr = 9
    while n > 0:
        n, digit = divmod(n, 10)
        if digit > curr:
            return False
        curr = digit
    return True

def solve(n):
    for i in xrange(n, -1, -1):
        if is_tidy(i):
            return i
    return -1

if __name__ == '__main__':
    main()

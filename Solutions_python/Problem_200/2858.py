def tidy(n):
    digits = list(map(int, str(n)))
    N = len(digits)

    i = 0

    while i < N - 1 and digits[i] <= digits[i + 1]:
        i += 1

    if i == N - 1:
        return n

    for j in range(i + 1, N):
        digits[j] = 9

    while i > 0 and digits[i] == digits[i - 1]:
        digits[i] = 9
        i -= 1

    digits[i] -= 1

    m = int(''.join(map(str, digits)))

    return m


def main():
    for _ in range(int(input())):
        print('Case #%d: %d' % (_ + 1, tidy(int(input()))))

if __name__ == '__main__':
    main()

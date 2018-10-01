import math


def main():
  T = int(raw_input())
  for i in range(T):
      N = int(raw_input())

      result = run_case(N)
      print 'Case #{}: {}'.format(i+1, result)


def run_case(n):
    while n > 0:
        x = get_tidy_or_next(n)
        if x == -1:
            return n
        n = x


def first_index_non_decreasing(L):
    pairs = zip(L, L[1:])
    for i, (x, y) in enumerate(pairs):
        if x > y:
            return len(L) - i - 2
    return -1


def get_place(n, i):
    m = 10 ** (i+1)
    return (n % m) / (m / 10)


def to_digits(n):
    num_digits = int(math.floor(math.log10(n) + 1))
    return [get_place(n, num_digits - x - 1) for x in range(num_digits)]


def get_tidy_or_next(n):
    """Returns either -1 (tidy) or the next highest number that may be tidy."""
    x = first_index_non_decreasing(to_digits(n))
    if x == -1:
        return -1

    return n - (n % 10 ** (x + 1)) - 1


if __name__ == '__main__':
    main()

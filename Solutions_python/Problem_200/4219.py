# go from right to left setting numbers to 9 and decrementing the next number

import math


def set_nines(n):
    value = 0
    for i in range(0, n+1):
        value += pow(10, i)*9

    return value


def solve(n):
    value = 0

    for i in range(0, int(math.log(n,10)+1)):
        a = n % 10
        n = int(n / 10)
        b = n % 10
        if a < b:
            value = set_nines(i)
            n = n-1
        else:
            value += pow(10, i) * a
    return value


def main():
    t = int(input())
    for i in range(0, t):
        n = int(input())
        print("Case #{}: {}".format(i+1, solve(n)))

if __name__ == "__main__":
    main()

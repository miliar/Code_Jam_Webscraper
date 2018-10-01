import math


def main():
    t = int(input())

    for c in range(t):
        n, k = map(int, input().split())

        size = get(n, k)
        if size <= 1:
            print(f"Case #{c + 1}: 0 0")
        else:
            print(f"Case #{c + 1}: {math.ceil((size - 1) / 2)} {math.floor((size - 1) / 2)}")


def get(n, k):
    level = math.floor(math.log(k) / math.log(2))
    peoples = math.pow(2, level)
    steels = n - peoples + 1
    good = math.ceil(steels / peoples)
    bad = math.floor(steels / peoples)
    x = steels - bad * peoples
    if k - math.pow(2, level) + 1 <= x:
        return good
    else:
        return bad


if __name__ == '__main__':
    main()

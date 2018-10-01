def ok(n):
    s = str(n)
    copy = "".join(sorted(list(s)))
    return copy == s


def test(test_nr):
    n = int(input())
    answer = None
    if ok(n):
        answer = n
    else:
        for i in range(19):
            number = n // (10 ** i)
            number = number * (10 ** i) - 1
            if ok(number):
                answer = number
                break
    print("Case #{}: {}".format(test_nr, answer))


if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        test(i + 1)

def main():
    number_of_cases = int(input())
    for case in range(1, number_of_cases + 1):
        start = input()

        x = list(start[::-1])

        last_nine_index = -1
        last_seen_digit = int(x[0])
        for i, c in enumerate(x):
            d = int(c)
            if d > last_seen_digit:
                last_seen_digit = d - 1
                x[i] = str(last_seen_digit)
                for j in range(last_nine_index + 1, i):
                    x[j] = "9"
                last_nine_index = i - 1
            else:
                last_seen_digit = d

        max_found = ''.join(x)[::-1]
        print("Case #{0:d}: {1:d}".format(case, int(max_found)))


if __name__ == '__main__':
    main()

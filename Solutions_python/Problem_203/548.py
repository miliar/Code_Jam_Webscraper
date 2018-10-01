import sys


def process_cake(cake, R, C):
    output = []
    # print(cake)
    # spread by row
    for row in cake:
        if row == C*"?":
            output.append(row)
        else:
            temp = ""
            c_initial = "?"
            for idx, initial in enumerate(row):
                if initial != "?" and c_initial == "?":
                    c_initial = initial
                    temp += initial*(idx+1)
                elif initial == "?" and c_initial != "?":
                    temp += c_initial
                elif initial != "?":
                    temp += initial
                    c_initial = initial
            output.append(temp)

    # spread over colnums
    final_output = []
    c_row = C*"?"
    for idx, row in enumerate(output):
        if row != C*"?" and c_row == C*"?":
            c_row = row
            for _ in range(idx+1):
                final_output.append(row)
        elif row == C*"?" and c_row != C*"?":
            final_output.append(c_row)
        elif row != C*"?":
            final_output.append(row)
            c_row = row

    return final_output


def print_case(i, output):
    print("Case #{}:".format(i))
    for line in output:
        print(line)


def main():
    T = int(sys.stdin.readline())

    for t in range(T):
        R, C = (int(i) for i in sys.stdin.readline().split())
        cake = []
        for r in range(R):
            cake.append(sys.stdin.readline().rstrip("\n"))
        output = process_cake(cake, R, C)
        print_case(t+1, output)


if __name__ == '__main__':
    main()



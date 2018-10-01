import sys

if __name__ == '__main__':

    test_cases = int(sys.stdin.readline().strip())

    for i in range(test_cases):
        row_num = int(sys.stdin.readline().strip())

        rows = []
        for j in range(4):
            row = map(int, sys.stdin.readline().strip().split())
            rows.append(row)

        numbers = rows[row_num - 1]

        row_num = int(sys.stdin.readline().strip())

        rows = []
        for j in range(4):
            row = map(int, sys.stdin.readline().strip().split())
            rows.append(row)

        numbers2 = rows[row_num - 1]

        v = set(numbers2).intersection(numbers)

        if len(v) == 1:
            print "Case #{}: {}".format(i + 1, list(v)[0])
        elif v:
            print "Case #{}: Bad magician!".format(i + 1)
        else:
            print "Case #{}: Volunteer cheated!".format(i + 1)

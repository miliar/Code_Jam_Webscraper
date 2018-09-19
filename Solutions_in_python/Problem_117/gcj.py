"""gcj"""

def solve_a():
    """solveA"""

    def check(table, c, i0, j0, di, dj):
        """check"""
        for k in xrange(4):
            i = i0 + k * di
            j = j0 + k * dj
            if table[i][j] == "T":
                continue
            if table[i][j] != c:
                return False
        return True

    def check2(table, c):
        """check2"""

        for i in xrange(4):
            if check(table, c, i, 0, 0, 1):
                return True
        for j in xrange(4):
            if check(table, c, 0, j, 1, 0):
                return True
        if check(table, c, 0, 0, 1, 1):
            return True
        if check(table, c, 0, 3, 1, -1):
            return True
        return False

    with open("A-large.in") as in_file:
        with open("A-out", "w+") as out_file:
            num_cases = int(in_file.readline())

            for case_index in xrange(num_cases):
                table = []
                for _ in xrange(4):
                    table.append(in_file.readline())
                in_file.readline()

                result = "Draw"
                has_winner = False
                if (not has_winner) and check2(table, "X"):
                    result = "X won"
                    has_winner = True
                if (not has_winner) and check2(table, "O"):
                    result = "O won"
                    has_winner = True
                if not has_winner:
                    for i in xrange(4):
                        has_moves = False
                        for j in xrange(4):
                            if table[i][j] == ".":
                                has_moves = True
                                result = "Game has not completed"
                                break
                        if has_moves:
                            break

                out_file.write(
                    "Case #" + str(case_index + 1) + ": " + result + "\n"
                )

def solve_b():
    """solve_b"""

    import time

    def check(table, width, height, test_i, test_j):
        """check"""

        has_hor_max = False
        for i in xrange(0, width):
            if i != test_i:
                if table[i][test_j] > table[test_i][test_j]:
                    has_hor_max = True
                    break

        has_ver_max = False
        for j in xrange(0, height):
            if j != test_j:
                if table[test_i][j] > table[test_i][test_j]:
                    has_ver_max = True
                    break

        if has_hor_max and has_ver_max:
            return False

        return True

    start = time.time()

    with open("B-large.in") as in_file:
        with open("B.out", "w+") as out_file:
            num_cases = int(in_file.readline())

            for case_index in xrange(num_cases):
                (width, height) = tuple(
                    [int(i) for i in in_file.readline().split()]
                )

                table = []
                for _ in xrange(width):
                    table.append([int(i) for i in in_file.readline().split()])

                is_possible = True
                for i in xrange(width):
                    for j in xrange(height):
                        if not check(table, width, height, i, j):
                            is_possible = False
                            break
                    if not is_possible:
                        break

                result = "NO"
                if is_possible:
                    result = "YES"
                out_file.write(
                    "Case #" + str(case_index + 1) + ": " + result + "\n"
                )

                print("Case #" + str(case_index + 1) + ": Done")

    print(time.time() - start)

def main():
    """main"""
    solve_b()

if __name__ == "__main__":
    main()
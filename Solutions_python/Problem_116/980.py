

def solve(array):
    # check for 4 in a row horizontal
    in_progress = False
    for row in array:
        if row.replace("T", "X") == "XXXX":
            return "X won"
        elif row.replace("T", "O") == "OOOO":
            return "O won"

    # check for 4 in a row vertical
    for i in xrange(4):
        row = "".join(zip(*array)[i])
        # print row
        if row.replace("T", "X") == "XXXX":
            return "X won"
        elif row.replace("T", "O") == "OOOO":
            return "O won"

    # diagonal 2 possible ways to win diagonally, from each corner
    # brute force? make it look nicer in the morning

    row = "".join((array[0][0], array[1][1], array[2][2], array[3][3]))
    row2 = "".join((array[0][3], array[1][2], array[2][1], array[3][0]))
    if row.replace("T", "X") == "XXXX" or row2.replace("T", "X") == "XXXX":
        return "X won"
    elif row.replace("T", "O") == "OOOO" or row2.replace("T", "O") == "OOOO":
        return "O won"
    for row in array:
        if row.find('.') is not -1:
            in_progress = True
            break
    if in_progress:
        return "Game has not completed"
    else:
        return "Draw"


def parse():
    with open("input", "r") as f_input, open("output", "w") as f_output:
        total_cases = int(f_input.readline())
        for case_num in xrange(total_cases):
            c1 = f_input.readline().strip()
            c2 = f_input.readline().strip()
            c3 = f_input.readline().strip()
            c4 = f_input.readline().strip()
            f_input.readline()
            result = solve([c1, c2, c3, c4])
            out = "Case #{}: {}".format(case_num + 1, result)
            f_output.write(out + "\n")

    pass


if __name__ == '__main__':
    parse()
    # c1 = 'XXXT'
    # c2 = '....'
    # c3 = 'OO..'
    # c4 = '....'
    # print solve([c1, c2, c3, c4])

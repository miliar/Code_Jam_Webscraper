import sys

def find_card(choice1, matrix1, choice2, matrix2):
    row_choice1 = set(matrix1[choice1 - 1])
    row_choice2 = set(matrix2[choice2 - 1])

    common_cards = row_choice1.intersection(row_choice2)

    if len(common_cards) == 1:
        return str(list(common_cards)[0])
    elif len(common_cards) == 0:
        return "Volunteer cheated!"
    else:
        return "Bad magician!"


if __name__ == '__main__':
    num_cases = int(sys.stdin.readline().strip())
    for c_n in xrange(num_cases):
        choice1 = int(sys.stdin.readline().strip())
        matrix1 = []
        for i in xrange(4):
            row = map(int, sys.stdin.readline().strip().split())
            matrix1.append(row)


        choice2 = int(sys.stdin.readline().strip())
        matrix2 = []
        for i in xrange(4):
            row = map(int, sys.stdin.readline().strip().split())
            matrix2.append(row)

        trick_result = find_card(choice1, matrix1, choice2, matrix2)
        print "Case #%d: %s" % (c_n + 1, trick_result)

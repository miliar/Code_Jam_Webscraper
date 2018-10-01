#!/usr/bin/env python2


def test_line(line):
    winner = ''
    ok = True
    x = 0
    while x < 4 and ok:
        c = line[x]

        if c == '.':
            ok = False
            break
        if c == 'T':
            x += 1
            continue
        if not winner:
            winner = c

        ok = winner == c
        x += 1
    return ok, winner


def resolv(case):
    # Rotate the board
    rotated_case = zip(*case[::-1])
    # Diagonales
    diag1 = [cell for y, line in enumerate(rotated_case)
             for x, cell in enumerate(line) if x == y]
    diag2 = [cell for y, line in enumerate(rotated_case)
             for x, cell in enumerate(line) if x == (3-y)]


    # Test every case
    everycase = case + rotated_case + [diag1, diag2]
    for line in everycase:
        ok, winner = test_line(line)
        if ok:
            return winner

    if '.' in [cell for line in case for cell in line]:
        return 'G'
    return 'D'

if __name__ == "__main__":
    ncase = int(raw_input())
    for n in range(ncase):
        case = [[c for c in raw_input()] for i in range(4)]
        result = resolv(case)
        if result == 'X':
            print("Case #" + str(n+1) + ": X won")
        elif result == 'O':
            print("Case #" + str(n+1) + ": O won")
        elif result == 'D':
            print("Case #" + str(n+1) + ": Draw")
        elif result == 'G':
            print("Case #" + str(n+1) + ": Game has not completed")
        else:
            print("-----------------FALID-----------------" + result)
        raw_input()


CHEAT = -1
BAD = -2
INPUT = "A-small-attempt0.in"
OUTPUT = "out.txt"

def main():
    in_f = open(INPUT, 'r')
    out_f = open(OUTPUT, 'w')
    T = int(in_f.readline())
    for case in range(1, T+1):
        r1 = int(in_f.readline())
        grid1 = []
        for i in range(4):
            grid1.append(map(int, in_f.readline().split()))
        r2 = int(in_f.readline())
        grid2 = []
        for i in range(4):
            grid2.append(map(int, in_f.readline().split()))
        card = solve(r1, grid1, r2, grid2)
        out_f.write("Case #" + str(case) + ": ")
        if card == BAD:
            out_f.write("Bad magician!\n")
        elif card == CHEAT:
            out_f.write("Volunteer cheated!\n")
        else:
            out_f.write(str(card) + "\n")

    in_f.close()
    out_f.close()

def solve(r1, grid1, r2, grid2):
    cards1 = grid1[r1 - 1]
    cards2 = grid2[r2 - 1]
    intersect = [card for card in cards1 if card in cards2]

    # print 'r1 = ' + str(r1)
    # print 'cards1 = ', cards1
    # print 'r1 = ' + str(r1)
    # print 'cards2 = ', cards2
    # print 'intersect = ', intersect


    if len(intersect) == 0:
        return CHEAT
    elif len(intersect) > 1:
        return BAD
    else:
        return intersect[0]

main()

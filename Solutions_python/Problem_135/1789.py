import os

if __name__ == "__main__":
    f = open("A-small-attempt0.in", "r")
    fout = open("A.out", "w")
    t = int(f.readline())
    for i in range(t):
        game1 = {}
        row1 = int(f.readline()) - 1
        for j in range(4):
            line = f.readline()
            game1[j] = [int(x) for x in line.strip().split()]
        game2 = {}
        row2 = int(f.readline()) - 1
        for j in range(4):
            line = f.readline()
            game2[j] = [int(x) for x in line.strip().split()]

        res = {}
        for j in game1[row1]:
            if j in res:
                res[j] += 1
            else:
                res[j] = 1
        for j in game2[row2]:
            if j in res:
                res[j] += 1
            else:
                res[j] = 1
        final = -1
        case = 0
        for j in res:
            if res[j] == 2:
                if final >= 0:
                    case = 1
                    break
                final = j
                case = 2
        if case == 0:
            fout.write("Case #%d: Volunteer cheated!\n" % (i+1))
        elif case == 1:
            fout.write("Case #%d: Bad magician!\n" % (i+1))
        else:
            fout.write("Case #%d: %d\n" % (i+1, final))
    fout.close()



import os

def checkXRC(X, R, C):
    if X >= 7:
        return False
    if (R*C) % X != 0:
        return False
    if min(R, C) < (X+1)/2:
        return False
    if X > 2 and X % 2 == 0 and min(R, C) == X / 2:
        return False
    return True

if __name__ == "__main__":
    fin = open("D-small-attempt1.in", "r")
    fout = open("D.out", "w")
    T = int(fin.readline())
    for t in range(T):
        t += 1
        line = fin.readline().strip()

        X, R, C = line.split()
        X = int(X)
        R = int(R)
        C = int(C)

        result = checkXRC(X, R, C)
        if result:
            fout.write("Case #%d: GABRIEL\n" % (t))
        else:
            fout.write("Case #%d: RICHARD\n" % (t))
    fout.close()


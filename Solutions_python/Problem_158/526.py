def f(x, r, c):
    if x == 4:
        if r * c == 8:
            return True
    if x > r * c:
        return True
    elif x == r * c and x >= 3:
        return True
    if r * c % x:
        return True
    if x > r and x > c:
        return True
    return False


fin = open('D-small-attempt1.in')
fout = open('D-small-attempt1.out', 'w')
n = int(fin.readline())
for i in range(n):
    x, r, c = map(int, fin.readline().split())
    if f(x, r, c):
        fout.write("Case #" + str(i + 1) + ": " + "RICHARD" + "\n")
    else:
        fout.write("Case #" + str(i + 1) + ": " + "GABRIEL" + "\n")
fin.close()
fout.close()

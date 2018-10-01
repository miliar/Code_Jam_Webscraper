
import fileinput

inp = fileinput.input()
def _():
    global inp
    return inp.readline()

T = int(_())
for case in range(T):
    row1 = int(_()) - 1
    rows1 = []
    for row in range(4):
        rows1.append(set(_().split()))
    row2 = int(_()) - 1
    rows2 = []
    for row in range(4):
        rows2.append(set(_().split()))
    possible = rows1[row1] & rows2[row2]
    num = len(possible)
    if num == 0:
        print "Case #" + str(case + 1) + ": Volunteer cheated!"
    elif num == 1:
        print "Case #" + str(case + 1) + ": " + list(possible)[0]
    else:
        print "Case #" + str(case + 1) + ": Bad magician!"
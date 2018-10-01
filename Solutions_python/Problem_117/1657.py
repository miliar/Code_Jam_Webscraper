f = open("B-small-attempt0.in")
lines = f.readlines()

cases = int(lines[0])
current = 1


def check(lawn, h1, h2):
    clone = [h2]*len(lawn[0])
    clone = [clone]*len(lawn)

    #check each row
    for i in range(len(lawn)):
        if straight(lawn[i]) and lawn[i][0] == h1:
            clone[i] = [h1]*len(clone[i])

    #check each column
    for i in range(len(lawn[0])):
        c = []
        for each in lawn:
            c += each[i]
        if straight(c) and c[0] == h1:
            for each in clone:
                each[i] = h1

    if clone == lawn:
        print "YES"
    else:
        print "NO"
                


def straight(l):
    if len(set(l)) == 1:
        return True
    else:
        return False

for c in range(1,cases+1):
    dim = lines[current].split()
    lawn = []
    for i in range(int(dim[0])):
        lawn += [lines[current+i+1].split()]
    h = sorted(set( [j for i in lawn for j in i]))
    print "Case #" + str(c) + ":",
    if len(h) == 1:
        h += [int(h[0]) + 1]
    check(lawn, h[0], h[1])
    current += int(dim[0])+1

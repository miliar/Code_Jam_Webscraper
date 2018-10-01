import math

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    ac, aj = [int(x) for  x in  input().split(" ")]  # read a list of integers, 2 in this case
    n = ac + aj
    p = []
    for i2 in range(0, ac):
        ci, di = [int(x) for x in  input().split(" ")]  # read a list of integers, 2 in this case
        p.append((ci, di, 0))

    for i2 in range(0, aj):
        ci, di = [int(x) for x in  input().split(" ")]  # read a list of integers, 2 in this case
        p.append((ci, di, 1))

    p.sort()

    amin = 720
    bmin = 720

    a = []
    b = []
    ab = []
    for i2 in range(0, n):
        first = p[i2]
        second = p[(i2 + 1) % n]

        if first[2] == 0:
            amin -= (first[1] - first[0]) % (24 * 60)

        if first[2] == 1:
            bmin -= (first[1] - first[0]) % (24 * 60)

        diff = (second[0] - first[1]) % (24 * 60)
        #print(first)
        #print(second)
        #print(diff)


        if first[2] == 0 and second[2] == 0:
            a.append(diff)
        elif first[2] == 1 and second[2] == 1:
            b.append(diff)
        else:
            ab.append(diff)

    #print(a)
    #print(b)
    #print(ab)

    a.sort()
    b.sort()


    afill = 0
    bfill = 0

    for aspan in a:
        if aspan <= amin:
            afill += 1
            amin -= aspan
        else:
            break

    for bspan in b:
        if bspan <= bmin:
            bfill += 1
            bmin -= bspan
        else:
            break

    arest = len(a) - afill
    brest = len(b) - bfill

    switches = arest * 2 + brest * 2 + len(ab)

    print("Case #{}: {}".format(i, switches))

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    Ac, Aj = [int(s) for s in input().strip().split()]
    aclist = []
    ajlist = []
    minAc = 1440
    for j in range(Ac):
        ci, di = [int(s) for s in input().strip().split()]  # read a list of integers, 2 in this case
        #if ci < minAc:
    #        minAc = ci
        aclist.append((ci, di))
    #aclist = list(map(lambda couple: [couple[0] - minAc, couple[1] - minAc], aclist))
    aclist = sorted(aclist, key=lambda x: x[0])
    minAj = 1440
    for j in range(Aj):
        ci, di = [int(s) for s in input().strip().split()]  # read a list of integers, 2 in this case
    #    if ci < minAc:
    #        minAj = ci
        ajlist.append((ci, di))
    #ajlist = list(map(lambda couple: [couple[0] - minAj, couple[1] - minAj], ajlist))
    ajlist = sorted(ajlist, key=lambda x: x[0])
    if Ac + Aj == 1:
        print("Case #%s: %s" % (i, 2))
        continue
    if Ac == 2:
        if abs(aclist[1][1] - aclist[0][0]) <= 720:
            print("Case #%s: %s" % (i, 2))
        elif abs(aclist[1][0] - aclist[0][1]) >= 720:
            print("Case #%s: %s" % (i, 2))
        else:
            print("Case #%s: %s" % (i, 4))
        continue
    if Aj == 2:
        if ajlist[1][1] - ajlist[0][0] <= 720:
            print("Case #%s: %s" % (i, 2))
        elif abs(ajlist[1][0] - ajlist[0][1]) >= 720:
            print("Case #%s: %s" % (i, 2))
        else:
            print("Case #%s: %s" % (i, 4))
        continue
    print("Case #%s: %s" % (i, 2))

    # check out .format's specification for more formatting options

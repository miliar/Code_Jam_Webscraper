file = open("A-small.in")
file.readline()
lines = file.read().splitlines()
file.close()
file = open("A-small.out", "w")

def initList():
    snapper_l = []
    for i in range(30):
        snapper_l.append(0)
    snapper_l[0] = 1
    return snapper_l

def isOn(snappers, snaps):
    snapper_l = initList()
    min_snaps = 0

    while min_snaps <= snaps and snapper_l[snappers - 1] is not 3:
        if snapper_l[0] is 1: snapper_l[0] = 3
        else: snapper_l[0] = 1
        for i in range(1, snappers):
            if snapper_l[i] is 0 and snapper_l[i-1] is 3:
                snapper_l[i] = 1
            elif snapper_l[i] is 1:
                if snapper_l[i-1] is 3: snapper_l[i] = 3
                else: snapper_l[i] = 2
            elif snapper_l[i] is 2:
                if snapper_l[i-1] is 3: snapper_l[i] = 3
            elif snapper_l[i] is 3:
                if snapper_l[i-1] is 3: snapper_l[i] = 1
                else: snapper_l[i] = 0
        #print snapper_l
        min_snaps += 1
    #print min_snaps
    #exit()
    if snaps is 0: return False
    if (snaps + 1) % (min_snaps + 1) is 0: return True
    return False

for case, line in enumerate(lines):
    snappers, snaps = line.split()
    file.write("Case #" + str(case +  1) + ":")
    if isOn(int(snappers), int(snaps)):
        file.write(" ON\n")
    else:
        file.write(" OFF\n");

file.close()

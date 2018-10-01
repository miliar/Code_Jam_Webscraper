def is_solvable(armin, motes):
    new_armin = armin
    for i in range(len(motes)):
        if motes[i] < new_armin:
            new_armin += motes[i]
        else:
            return (motes[i], new_armin, i)
    return (0, 0, 0)


def complete(armin, motes, i):
    motes = sorted(motes)
    #print armin, motes
    mote, new_armin, x = is_solvable(armin, motes)
    if mote == 0:
        #print("done")
        return i
    else:
        new_motes = motes[x:]
        p = 0
        sums = 0
        for j in range(len(new_motes)):
            sums = 2**(j + 1) * new_armin - (j + 1)
            if sums > new_motes[0]:
                #print(j)
                p = j + 1
                break
        if new_armin != 1 and p > 0 and p < len(new_motes):
            # add
            #print("add")
            new_motes.append(new_armin - 1)
            return complete(new_armin, new_motes, i + 1)
        else:
            #print("delete")
            new_motes.remove(mote)
            return complete(new_armin, new_motes, i + 1)


if __name__ == '__main__':
    #print complete(2, [2, 1, 1, 6])
    f = open( "A-small-attempt3.in", "r" )
    cases = f.readline().strip();
    for i in range(int(cases)):
        line = f.readline().strip()
        armin = int(line.split()[0])
        motes = [int(x) for x in f.readline().strip().split()]
        print("Case #%d: %s" % (i+1, complete(armin, motes, 0)))


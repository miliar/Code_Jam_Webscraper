def eat_motes(armin, motes):
    copy = motes[:]
    for mote in copy:
        if armin > mote:
            armin += mote
            motes.remove(mote)
    return armin, motes


def growth(armin, mote):
    times = 0
    while armin <= mote:
        armin = 2*armin - 1
        times += 1
    return armin, times


def edible(armin, motes):
    eaten = 0
    for mote in motes:
        if armin > mote:
            armin += mote
            eaten += 1
        else:
            break
    return eaten


def minimum(a, b):
    if a < b:
        return a
    else:
        return b


def move_motes(armin, motes):
    changes1 = 0
    changes2 = -1
    if armin == 1:
        return len(motes)
    armin, motes = eat_motes(armin, motes)
    while motes:
        armin, times = growth(armin, motes[0])
        if changes2 == -1:
            changes2 = changes1 + len(motes)
        else:
            changes2 = minimum(changes1 + len(motes), changes2)
        changes1 += times
        armin, motes = eat_motes(armin, motes)
    if changes2 == -1:
        return changes1
    else:
        return minimum(changes1, changes2)


#print(move_motes(10, [9, 20, 25, 1000]))
#print(move_motes(2, [1, 2]))
#print(move_motes(10, [9, 20, 25, 100]))
#print(move_motes(1, [1, 1, 1, 1]))

cases = int(input())
for i in range(1, cases+1):
    armin = list(map(int, input().split(' ')))[0]
    motes = list(map(int, input().split(' ')))
    motes.sort()
    print("Case #" + str(i) + ":", move_motes(armin, motes))

def solve(boosters, buildtime, target, spacings):
    star = 0
    # Calculate the total journey time before boosters
    before = 0
    while before < buildtime and star < target:
        before += spacings[star % len(spacings)] * 2
        star += 1
    # If we are done return the current time
    if star == target:
        return before
    # Add the partial booster journey after the boosters are built
    after = [before - buildtime]
    # Add the remaining journeys
    while star < target:
        after += [spacings[star % len(spacings)] * 2]
        star += 1
    # Half the time for all of the journeys we have boosters for
    boosted = [-1 for i in after]
    while sum(boosted) < 0 and boosters > 0:
        # Find the longest unboosted journey
        longest = -1
        length = -1
        for i in range(len(after)):
            if boosted[i] == -1 and after[i] > length:
                longest = i
                length = after[i]
        # Block this journey from being boosted again
        boosted[longest] = 0
        # Half this journey time
        after[longest] = after[longest] / 2
        # Remove a booster
        boosters -= 1
    # Sum the full journey time and return
    return buildtime + sum(after)

f = file("input.txt")
lines = f.readlines()
for tc in range(1, int(lines[0]) + 1):
    data = [int(datum) for datum in lines[tc].split(" ")]
    b = data[0]
    bt = data[1]
    t = data[2]
    s = data[4: 4 + data[3]]
    print "Case #" + str(tc) + ": " + str(solve(b, bt, t, s))

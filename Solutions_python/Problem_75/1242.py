number_of_cases = int(raw_input())
for i in range(1, number_of_cases + 1):
    s = raw_input()
    instructions = s.split()

    comb = {}
    clear = {}

    number_comb = int(instructions.pop(0))

    for k in range(0, number_comb):
        tt = instructions.pop(0)
        comb[tt[0:2]] = tt[2]
        comb[tt[1]+tt[0]] = tt[2]

    number_clear = int(instructions.pop(0))

    for k in range(0, number_clear):
        tt = instructions.pop(0)
        clear[tt[0]] = tt[1]
        clear[tt[1]] = tt[0]

    length_string = instructions.pop(0)

    magi = instructions.pop(0)

    f = []
    letter_count = {}

    for xxx in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        letter_count[xxx] = 0

    for s in magi:
        letter_count[s] = letter_count[s] + 1
        f.append(s)
        while len(f) > 1 and comb.has_key("".join(f[-2:])):
            c = comb["".join(f[-2:])]
            letter_count[c] += 1
            letter_count[f.pop()] -= 1
            letter_count[f.pop()] -= 1
            f.append(c)
        if clear.has_key(f[-1]) and letter_count[clear[f[-1]]] > 0:
            f = []
            for xxx in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                letter_count[xxx] = 0

    print "Case #" + str(i) + ": [" + ", ".join(f) + "]"

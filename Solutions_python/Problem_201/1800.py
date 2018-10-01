class Pair:
    start = 0
    length = 1


def count_left(stalls, index):
    if index == 0:
        return 0

    res = 0
    while stalls[index - res - 1]:
        res += 1
    return res


def count_right(stalls, index):
    if index >= len(stalls):
        return 0

    res = 0
    while stalls[index + res + 1]:
        res += 1
    return res


def process(stalls, entering):
    # init, True = free stall
    S = [True] * (stalls + 2)
    S[0] = False
    S[-1] = False
    last_index = -1
    for i in range(entering):
        pairs = []
        maxlength = 1
        con = False
        for j in range(len(S)):
            if S[j]:
                if con:
                    pairs[-1].length += 1
                    if pairs[-1].length > maxlength:
                        maxlength = pairs[-1].length
                else:
                    p = Pair()
                    p.start = j
                    pairs += [p]
                    con = True

            else:
                con = False

        # get biggest pairs
        big = []
        for pair in pairs:
            if pair.length == maxlength:
                big += [pair]

        index = -1
        if big[0].length % 2 == 0:
            index = big[0].start + (big[0].length // 2) - 1
        else:
            index = big[0].start + (big[0].length // 2)
        S[index] = False
        last_index = index
    maxLR = max(count_left(S, last_index), count_right(S, last_index))
    minLR = min(count_left(S, last_index), count_right(S, last_index))
    return str(maxLR) + " " + str(minLR)



inp = open("input/C-small-1-attempt0.in", "r")
out = open("output/C-small-1.out", "w")
lines = inp.read().split("\n")
line_count = int(lines[0])

for i in range(1, line_count + 1):
    tmp = lines[i].split(" ")
    stalls = int(tmp[0])
    entering = int(tmp[1])
    out.write("Case #" + str(i) + ": " + str(process(stalls, entering)) + "\n")



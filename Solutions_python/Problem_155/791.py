__author__ = 'rrampage'

t = int(input())


def input_format():
    s = input().split()[1]
    return [int(i) for i in s]


def ovation(aud):
    extras = 0
    tot_standing = 0
    for i, a in enumerate(aud):
        if a == 0:
            continue
        if tot_standing >= i:
            tot_standing += a
        else:
            extras += (i - tot_standing)
            tot_standing += (i - tot_standing)
            tot_standing += a
    return extras

for x in range(t):
    print("Case #%d: %d" % (x+1, ovation(input_format())))
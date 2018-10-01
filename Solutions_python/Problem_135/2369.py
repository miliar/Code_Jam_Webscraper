import os

def main():
    f = open('A-small-attempt0.in')
    e = enumerate(f)

    count = int(e.next()[1])

    for i in range(count):
        res = test_it(i,e)
        print "Case #%d: %s"%(i+1, res)

def get_row(e):
    row = int(e.next()[1])

    card = [
        e.next()[1].split(),
        e.next()[1].split(),
        e.next()[1].split(),
        e.next()[1].split(),
    ]

    return card[row-1]


def test_it(idx, e):
    first = get_row(e)
    second = get_row(e)

    dup = []

    for x in first:
        if x in second:
            dup.append(x)

    if not dup:
        return 'Volunteer cheated!'

    if len(dup) != 1:
        return 'Bad magician!'

    return dup[0]

main()

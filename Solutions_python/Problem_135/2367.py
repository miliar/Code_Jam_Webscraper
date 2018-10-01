import itertools

cases = int(raw_input())
n = cases

results = []

while n > 0:
    spot_row1 = int(raw_input())
    row1 = [raw_input() for x in range(4)]

    spot_row2 = int(raw_input())
    row2 = [raw_input() for x in range(4)]

    chosen_row1 = map(int, row1[spot_row1 - 1].split(' '))
    chosen_row2 = map(int, row2[spot_row2 - 1].split(' '))

    c3 = filter(lambda x: x in chosen_row2, chosen_row1)

    if len(c3) == 1:
        results.append(c3[0])
    elif not len(c3):
        results.append('Volunteer cheated!')
    else:
        results.append('Bad magician!')

    n -= 1

for i in range(cases):
    print 'Case #%d: %s' % (i + 1, str(results[i]))
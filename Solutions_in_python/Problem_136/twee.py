fr = open('twee.in', 'r')
fw = open('twee.out', 'w')

N = int(fr.readline())
for n in range(1, N+1):
    C, F, X = map(float, fr.readline().strip().split(' '))

    total = 0.0
    rate = 2.0
    totals = []

    while True:
        totals.append(total + (X/rate))
        total += C/rate
        rate += F

        if len(totals) > 1:
            if totals[-1]> totals[-2]:
                break

    fw.write('Case #' + str(n) + ': ' + str(min(totals)) + '\n')

fr.close()
fw.close()

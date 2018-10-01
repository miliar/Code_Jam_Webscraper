__author__ = 'Levan Kasradze'

with open('b.in', 'r') as fin:
    with open('b.out', 'w') as fout:
        t = int(fin.readline())
        for i in range(1, t + 1):
            line = fin.readline().strip().split()
            c = float(line[0])
            f = float(line[1])
            x = float(line[2])

            sumC = 0.0
            speed = 2.0
            time = x / speed

            while True:
                sumC += c / speed
                speed += f
                tmp = sumC + x / speed
                if tmp < time:
                    time = tmp
                else:
                    break

            fout.write('Case #' + str(i) + ': ' + "%.7f" % time + '\n')
N = input()

for i in range(N):
    line = raw_input()
    line = map(int, list(line))

    while True:
        for j in range(len(line) - 1):
            if line[j] > line[j + 1]:
                for k in range(j + 1, len(line)):
                    line[k] = 9

                for k in range(j, -1, -1):
                    if line[k] > 0:
                        line[k] -= 1
                        break
                    line[k] = 9
                break
        else:
            break

    print 'Case #%d: %s' % (i + 1, ''.join(map(str, line)).lstrip('0'))


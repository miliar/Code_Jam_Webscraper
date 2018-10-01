f = open('input.in', 'r')

nInput = f.readline()
nInput = int(nInput)

nCase = 0



for line in f:
    line_spl = line.split(' ')
    signal = list(line_spl[0])
    flip_size = int(line_spl[1].replace('\n', ''))

    index = 0
    nFlip = 0

    last_head = len(signal) - flip_size

    while index <= last_head:
        if signal[index] == '-':
            for digit in list(range(index, index+flip_size)):
                if signal[digit] == '-':
                    signal[digit] = '+'
                else:
                    signal[digit] = '-'
            nFlip += 1
        index += 1

    isWorkable = True
    for i in list(range(last_head, len(signal))):
        if signal[i] == '-':
            isWorkable = False

    nCase += 1

    print("Case #", end='')

    print(str(nCase), end='')

    print(": ", end='')

    if isWorkable:
        print(nFlip, end='')

    else:
        print("IMPOSSIBLE", end='')

    print("\n", end='')


f.close()


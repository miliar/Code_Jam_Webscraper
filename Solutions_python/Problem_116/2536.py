def main():
    inFile = open('A-small-attempt0.in')
    outFile = open('ticTac.out.txt', 'w+')

    keyMap = {}
    keyMap['.'] = 0
    keyMap['X'] = 1
    keyMap['O'] = 1000
    keyMap['T'] = 50

    N = int(inFile.readline())

    for x in range(N):
        r = []
        c = [0, 0, 0, 0]
        d1 = 0
        d2 = 0
        incomplete = False
        for i in range(4):
            tokens = inFile.readline()[:-1]
            rSum = 0
            for j in range(4):
                n = tokens[j]
                incomplete = n == '.'
                rSum += keyMap.get(n)
                c[j] += keyMap.get(n)
                if i == j:
                    d1 += keyMap.get(n)
                if i + j == 3:
                    d2 += keyMap.get(n)
            r.append(rSum)
        winner = ''
        result = ''
        for k in range(4):
            if r[k] == 4 or r[k] == 53 or c[k] == 4 or c[k] == 53 or d1 == 4 or d1 == 53 or d2 == 4 or d2 == 53:
                winner = 'X'
                break
            elif r[k] == 4000 or r[k] == 3050 or c[k] == 4000 or c[k] == 3050 or d1 == 4000 or d1 == 3050 or d2 == 4000 or d2 == 3050:
                winner = 'O'
                break
        if winner == 'X' or winner == 'O':
            result = '%s won' % winner
        elif incomplete:
            result = 'Game has not completed'
        else:
            result = 'Draw'

        outFile.write('Case #%d: %s\n' % (x + 1, result))
        inFile.readline()

if __name__ == '__main__':
    main()

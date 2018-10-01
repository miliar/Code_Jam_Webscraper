
if __name__ == '__main__':
    inFile = open('B-large.in', 'r')
    outFile = open('B-large.out', 'w')
    numCases = int(inFile.readline())
    print("Cases:", numCases)
    for case in range(numCases):
        outFile.write('Case #{0}: '.format(case + 1))
        data = inFile.readline().rsplit()
        print(data)

        numCombos = int(data.pop(0))
        combos = []
        for i in range(numCombos):
            combos.append(data.pop(0))
        print('combos', combos)

        numOppose = int(data.pop(0))
        oppose = []
        for i in range(numOppose):
            oppose.append(data.pop(0))
        print('oppose', oppose)

        invoke = data.pop(1)
        print('invoke', invoke)

        last = ''
        result = []
        for ch in invoke:
            for c in combos:
                if (c[0] == ch and c[1] == last) or (c[1] == ch and c[0] == last):
                    result[len(result)-1] = c[2]
                    last = c[2]
                    break
            else:
                for o in oppose:
                    if o[0] == ch:
                        if o[1] in result:
                            result = []
                            last = ''
                            break
                    elif o[1] == ch:
                        if o[0] in result:
                            result = []
                            last = ''
                            break
                else:
                    last = ch
                    result.append(ch)
        print('result', result)
        outFile.write(str(result).replace("'", '') + '\n')
    outFile.close()
    inFile.close()

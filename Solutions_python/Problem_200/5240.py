def mainTwo(lastNumber, caseNum):
    myList = list(range(lastNumber, 0, -1))
    lastValue = 0
    for x in myList:
        if len(str(x)) != 1:
            newNum = [int(d) for d in str(x)]
            if lastValue == 0:
                for i, _ in enumerate(newNum[:-1]):
                    valOne = newNum[i]
                    valTwo = newNum[i + 1]
                    if lastValue == 0:
                        if valOne > valTwo:
                            lastValue = 0
                            break
                        else:
                            if valTwo == newNum[-1]:
                                lastValue = x
                                break
                    else:
                        break
            else:
                break
        else:
            lastValue = x
            break
    print("Case #{0}: {1}".format(caseNum, lastValue))


if __name__ == "__main__":
    import fileinput

    f = fileinput.input()
    T = int(f.readline().strip())
    for case in range(1, T + 1):
        S = f.readline().strip()
        val = mainTwo(int(S), case)

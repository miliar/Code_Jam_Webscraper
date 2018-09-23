if __name__ == '__main__':
    testC = input()
    for i in range(int(testC)):
        # inputN = list(str(i))
        inputN = list(str(input()))
        tN = [int(d) for d in inputN]
        while sorted(tN) != tN:
            for i2, e in reversed(list(enumerate(tN))):
                if i2 > 0 and tN[i2-1] >= 0:
                    tN[i2] = 9
                    tN[i2-1] -= 1
                    if sorted(tN) == tN:
                        break
        print("Case #{0}: {1}".format(i + 1, int(''.join(str(s) for s in tN))))

def main():
    nCases = int(input())
    for case in range(nCases):
        poss = [0] * 16
        line = int(input()) - 1
        cards = []
        for i in range(4):
            cards.append(input())

        for c in cards[line].split(' '):
            n = int(c)
            poss[n - 1] = poss[n-1] + 1

        # Second card lot.
        cards = []
        line = int(input()) - 1
        for i in range(4):
            cards.append(input())

        for c in cards[line].split(' '):
            n = int(c)
            poss[n - 1] = poss[n-1] + 1

        twos = 0
        chosen = 0
        for i in range(len(poss)):
            if poss[i] > 1:
                twos = twos + 1
                chosen = i + 1

        caseStr = 'Case #' + str(case + 1) + ':'
        if twos == 1:
            print(caseStr, chosen)
        elif twos == 0:
            print(caseStr, 'Volunteer cheated!')
        elif twos > 1:
            print(caseStr, 'Bad magician!')


if __name__ == "__main__":
    main()

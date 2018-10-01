import pprint as pp


def main(file):
    """
    Runs magic trick to guess which card was picked by guest.
    """
    total, testcards = readin(file)
    print 'testcards'
    pp.pprint(testcards)
    allguess = []
    for testnum, test in testcards.items():
        allguess.append(guess(test))
    writeguess(allguess)


def writeguess(allguess):
    """
    Outputs results as same as codejam
    """
    with open('a_out.txt', 'w') as f:
        for ncase, g in enumerate(allguess):
            if len(g) == 1:
                f.write("Case #%s: %s\n" % (ncase+1, g[0]))
            elif len(g) > 1:
                f.write("Case #%s: Bad magician!\n" % (ncase+1))
            else:
                f.write("Case #%s: Volunteer cheated!\n" % (ncase+1))


def guess(test):
    """
    Guesses what number it is based on the 2 rows choosen.
    """
    first = test[0]
    second = test[1]
    choicea = first['a']
    rowa = chooserow(choicea, first['c'])
    choiceb = second['a']
    rowb = chooserow(choiceb, second['c'])
    return [u for u in rowa if u in rowb]


def chooserow(row, cards):
    """Chooses row from cards array. Corrected for non 0 index"""
    return cards[row-1]


def readin(afile):
    """
    Read input file
    """
    tests = {}
    with open(afile) as f:
        testcase = str2int(f.next())[0]
        for x in range(testcase):
            tests[x] = {}
            for y in range(2):
                tests[x][y] = {}
                answer = str2int(f.next())[0]

                tests[x][y]['a'] = answer
                cards = []
                for c in range(4):
                    cards.append(str2int(f.next()))
                tests[x][y]['c'] = cards
    return [testcase, tests]


def str2int(l):
    """
    Converts row of ints in file to array
    """
    cleanstr = l.strip()
    splitstr = cleanstr.split()
    intlist = [int(u) for u in splitstr]
    return intlist


if __name__ == "__main__":
    main("A-small-attempt0.in")
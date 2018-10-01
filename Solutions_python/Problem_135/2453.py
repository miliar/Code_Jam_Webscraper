f = file("A-small_input.txt", 'r').readlines()
numCases = int(f[0])
currentCase = 0

while currentCase < numCases:
    case = f[1+(currentCase*10):1+((currentCase+1)*10)]
    firstGuessRow = set(case[int(case[0])].strip().split(" "))
    secondGuessRow = set(case[int(case[5])+5].strip().split(" "))
    matches = firstGuessRow.intersection(secondGuessRow)
    matchAmount = len(matches)
    if matchAmount == 0:
        print "Case #%i: %s" % (currentCase+1, "Volunteer cheated!")
    elif matchAmount == 1:
        print "Case #%i: %i" % (currentCase+1, int(list(matches)[0]))
    else:
        print "Case #%i: %s" % (currentCase+1, "Bad magician!")
    currentCase += 1
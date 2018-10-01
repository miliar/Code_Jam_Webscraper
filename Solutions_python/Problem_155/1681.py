standing = open('standing.in', 'r')
results = open('standing.out', 'w')

caseNumber = int(standing.readline())
cases = []

for line in standing:
    cases.append(line.split())

currentCase = 1

for case in cases:
    shyMax = int(case[0])
    audience = case[1]
    friends = 0
    people = 0
    for shyLevel in xrange(0, shyMax):
        people += int(audience[shyLevel])
        if (people + friends) < shyLevel + 1:
            while (people + friends) < shyLevel + 1:
                friends += 1
    results.write('Case #' + str(currentCase) + ': ' + str(friends) + '\n')
    currentCase += 1
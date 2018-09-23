def f(activities, ac, aj):
    activities = sorted(activities)

    timeOfC = sum(act[1] - act[0] if act[2] == 'C' else 0 for act in activities)
    timeOfJ = sum(act[1] - act[0] if act[2] == 'J' else 0 for act in activities)

    intervalsOfC = []
    intervalsOfJ = []

    for i in range(len(activities)):
        act1 = activities[i-1]
        act2 = activities[i]

        if act1[2] == act2[2]:
            t = (act2[0] - act1[1])%1440

            if act1[2] == 'C':
                intervalsOfC.append(t)
            else:
                intervalsOfJ.append(t)

    merge = 0

    for t in sorted(intervalsOfC):
        timeOfC += t
        if timeOfC > 720:
            break

        merge += 1

    for t in sorted(intervalsOfJ):
        timeOfJ += t
        if timeOfJ > 720:
            break

        merge += 1

    numOfInterval = len(intervalsOfC) + len(intervalsOfJ) - merge

    return ac + aj - merge + numOfInterval


t = int(input())
for testCase in range(t):
    ac, aj = map(int, input().split())
    activities = []

    for i in range(ac):
        start, end = map(int, input().split())
        activities.append((start, end, 'C'))

    for i in range(aj):
        start, end = map(int, input().split())
        activities.append((start, end, 'J'))

    print('Case #' + str(testCase+1) + ':', f(activities, ac, aj))

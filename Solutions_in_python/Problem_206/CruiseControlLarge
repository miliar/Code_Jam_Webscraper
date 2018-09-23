def CruiseControl(D, N, horses):
    horsePositions = sorted(horses.keys())[::-1]
    time = (D - horsePositions[0])/horses[horsePositions[0]]
    for i in range(0, N - 1):
        newTime = (D - horsePositions[i+1])/horses[horsePositions[i+1]]
        time = max(time, newTime)

    return round(D/time, 6)


t = int(input())
for i in range(1, t + 1):
    params1 = input().split(" ")
    params1 = [int(k) for k in params1]
    horses = {}
    for j in range(params1[1]):
        horse = input().split(" ")
        horse = [int(k) for k in horse]
        horses[horse[0]] = horse[1]

    output = CruiseControl(params1[0], params1[1], horses)
    print("Case #{}: {}".format(i, output))

for i in range(int(input().strip())):
    length, numHorses = map(int,input().strip().split())
    maxTime = 0
    for j in range(numHorses):
        position, speed = map(int,input().strip().split())
        distanceRemaining = length - position
        timeNeeded = distanceRemaining / speed
        if maxTime == -1 or timeNeeded > maxTime:
            maxTime = timeNeeded
    print("Case #" + str(i+1) + ":",str(length / maxTime))

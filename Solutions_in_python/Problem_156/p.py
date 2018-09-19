def handle(D):
    durations = []
    for goalAmount in range(1, max(D) + 1):
        duration = goalAmount
        for amount in D:
            if amount > goalAmount:
                duration = duration + amount // goalAmount
                if amount % goalAmount == 0:
                    duration = duration - 1

        durations.append(duration)

    return min(durations)

t = int(input())
for i in range(t):
    d = int(input())
    c = list(map(int, input().split(" ")))
    print("Case #%d: %d" % (i + 1, handle(c)))

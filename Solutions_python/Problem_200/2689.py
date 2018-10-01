

def processMany():
    with open("/Users/ChesterAiGo/Desktop/BSmall.txt") as Doc:
        lines = [x.strip() for x in Doc.readlines()]

    for i in range(len(lines)):
        print("Case #{0}: {1}".format(i + 1, processOne(lines[i])))


def processOne(tc):
    N = int(tc)
    lastNumber = 1

    for i in range(N, 1, -1):
        if(isTidy(i)):
            lastNumber = i
            break

    return lastNumber


def isTidy(N):
    return sorted(str(N)) == list(str(N))


processMany()










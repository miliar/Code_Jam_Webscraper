import math
#yoloswag
def solve(mushrooms):
    f = int(mushrooms[0])
    a = 0;
    for i in range(1, len(mushrooms)):
        plate = int(mushrooms[i])
        diff = plate - f
        f = plate
        if(diff < 0):
            a -= diff

    #get greatest change
    biggestDiff = 0
    l = int(mushrooms[0])
    for i in range(1, len(mushrooms)):
        plate = int(mushrooms[i])
        diff = plate - l
        l = plate
        if(-diff > biggestDiff):
            biggestDiff = -diff
    #         print("Diff: ", biggestDiff)
    # print("Speed: ", biggestDiff)
    speed = biggestDiff
    b = 0
    leftOver = 0
    for i in range(0, len(mushrooms) - 1):
        plate = int(mushrooms[i])

        if(speed >= plate):
            b += plate
            leftOver = 0
            # print("empty plate", plate, b, leftOver)
        else:
            b += speed
            leftOver += plate - speed
            # print("leftover", plate, b, leftOver)
    # print(a, b)
    return [a, b]

inputs = open("input.txt").readlines()
output = open('out.txt', 'w')
t = int(inputs[0])
r = 0
for i in range(1, t + 1):
    r += 2
    mushrooms = inputs[r].rstrip().split(" ")
    #print(mushrooms)
    ans = solve(mushrooms)

    answer = "Case #%d: %d %d\n"%(i, ans[0], ans[1])
    print(answer)
    output.write(answer)
output.close()

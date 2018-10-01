def maxP(pairs):
    maxVal=0
    maxIndex=0
    index=0
    for p in pairs:
        if maxVal<math.ceil(p[0]/p[1]):
            maxVal=math.ceil(p[0]/p[1])
            maxIndex=index
        index+=1
    return [maxVal,maxIndex]

import math

fo = open("B-large.in")
fo2 = open("output2.txt", mode='w')
tests = eval(fo.readline())
output = []
for x in range(1, tests + 1):
    str1 = fo.readline().strip("\n")
    D = eval(str1)
    str1 = fo.readline().strip("\n")

    Pinput = str1.split(" ")
    Pinput = [int(i) for i in Pinput]

    pairs = []
    for p in Pinput:
        pairs.append([p, 1])

    sol = maxP(pairs)[0]
    specM = 0

    while (sol > specM):
        specM += 1

        curr=maxP(pairs)
        pairs[curr[1]][1]+=1
        sol = min(sol, specM + maxP(pairs)[0])

    output.append("Case #" + str(x) + ": " + str(sol) + "\n")

fo2.writelines(output)

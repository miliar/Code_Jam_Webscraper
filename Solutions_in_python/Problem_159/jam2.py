import re

test_count = input()

for i in range(0, test_count):
    n = input()
    stuffstring = raw_input()
    stuff = [int(j) for j in stuffstring.split()]

    lastq = -1
    mineat = 0
    for q in stuff:
        if lastq == -1:
            lastq = q
        else:
            mineat += max(lastq - q, 0)
            lastq = q

    largestq = -1
    lastq = -1
    for q in stuff:
        if lastq == -1:
            lastq = q
        else:
            largestq = max(lastq - q, largestq)
            lastq = q

    eatmethodtwo = 0
    for q in range(0, len(stuff)-1):
        eatmethodtwo += min(largestq, stuff[q])

    print "Case #" + str(i + 1) + ": " + str(mineat) + " " + str(eatmethodtwo)







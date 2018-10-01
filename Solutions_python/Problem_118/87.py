def go(pos):
    global halfLenX, lenX, X

    lenX2 = len(X)*2-1
    X2 = [0]*lenX2

    for i in range(lenX2):
        for j in range(i+1):
            if i-j < len(X) and j < len(X):
                X2[i] += X[j] * X[i-j]
        if (X2[i] > 9):
            break
    else:
        if pos != 0 and X[0] == 0:
            pass
        else:
            if (pos == halfLenX):
#                print "".join([str(val) for val in X])
                validX.append(int("".join([str(val) for val in X])))
            else:
                for v in range(10):
                    X[pos] = X[lenX-1-pos] = v
                    go(pos+1)
                    X[pos] = X[lenX-1-pos] = 0

validX = []

maxHalfLen = 26
#maxHalfLen = 15

try:
    f=open("preprocess")
    validX = eval(f.read())
    f.close()
except IOError:
    pass


if len(validX) == 0:
    for oddLenX in [0,1]:
        for halfLenX in xrange(1, maxHalfLen):
            lenX = 2*halfLenX - oddLenX
#            print "Len = " + str(lenX) + " (should be at most 50)"

            X = [0] * lenX

            go(0)


validX = sorted(validX)

f=open("preprocess", "w")
f.write(str(validX))
f.close()


validX2 = [x*x for x in validX]

ntest = int(raw_input())
for t in xrange(ntest):
    a,b = [int(x) for x in raw_input().split(" ")]

    result=0
    for num in validX2:
        if a <= num and num <= b:
            result += 1

    print "Case #" + str(t+1)+": " + str(result)

#for X in validX:
#    print str(X*X) + " -> " + str(X)


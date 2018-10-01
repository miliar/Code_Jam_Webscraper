def addComb(comb, order):
    if order:
        return (comb[0] + comb[1], comb[2])
    else:
        return (comb[1] + comb[0], comb[2])

def organise(q):
    q = q.split(" ")
    comb, opp = list(), list()

    numComb = int(q[0])
    q = q[1:]
    for i in range(numComb):
        comb.append(addComb(q[i], 0))
        if q[i][0] != q[i][1]: comb.append(addComb(q[i], 1))

    q = q[numComb:]

    numOpp = int(q[0])
    q = q[1:]
    for i in range(numOpp):
        opp.append((q[i][0], q[i][1]))

    q = q[numOpp+1:]

    return (comb, opp, q[0])

def tryCombining(result, comb):
    for c in comb:
        result = result.replace(c[0], c[1])
    return result

def tryOpposing(result, opp):
    for o in opp:
        if (o[0] in result) and (o[1] in result):
            return ""
    return result

def solve(q):  

    comb, opp, q = organise(q)

    result = ""

    for e in q:
        result += e
        result = tryCombining(result, comb)
        result = tryOpposing(result, opp)

    re = "["
    for r in result: re += r + ", "
    if re[-2:] == ", ": re = re[:-2]
    re += "]"

    return re

fIn     = open('aInput', 'r')
fOut    = open('aOutput', 'r+')

fIn = fIn.readlines()
fIn = fIn[1:]

for i in range(len(fIn)):
    e = fIn[i][:-1]
    fOut.write("Case #" + str(i+1) + ": " + solve(e) + "\n")

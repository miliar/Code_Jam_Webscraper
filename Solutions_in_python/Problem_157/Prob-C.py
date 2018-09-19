import sys
from math import sqrt, floor
f = open(sys.argv[1], 'r')

multable = {'1': {'1':'1','i':'i','j':'j','k':'k'},
 'i': {'1':'i','i':'-1','j':'k','k':'-j'},
 'j': {'1':'j','i':'-k','j':'-1','k':'i'},
 'k': {'1':'k','i':'j','j':'-i','k':'-1'}}

def multi(a, b):
    return multable[a][b]

numOfTest = int(f.readline())

for i in range(1, numOfTest + 1) :
    print("Case #" + str(i) + ":", end=' ')
    
    # read test case
    tc = f.readline().split(' ')
    l = int(tc[0])
    x = int(tc[1])
    part = f.readline()
    part = part[:len(part) - 1]

    if l * x < 3 :
        print("NO")
        continue

    mainStr = part * x

    isMinus = False
    go = False
    while len(mainStr) >= 3:
        if mainStr[0] == 'i' and not isMinus:
            mainStr = mainStr[1:]
            go = True
            break
        mulresult = multi(mainStr[0], mainStr[1])
        if mulresult[0] == '-':
            isMinus = not isMinus
            mulresult = mulresult[1:]
        mainStr = mulresult + mainStr[2:]
    if not go:
        print("NO")
        continue

    go = False
    while len(mainStr) >= 2:
        if mainStr[0] == 'j' and not isMinus:
            mainStr = mainStr[1:]
            go = True
            break
        mulresult = multi(mainStr[0], mainStr[1])
        if mulresult[0] == '-':
            isMinus = not isMinus
            mulresult = mulresult[1:]
        mainStr = mulresult + mainStr[2:]
    if not go:
        print("NO")
        continue

    go = False
    while len(mainStr) >= 2:
        mulresult = multi(mainStr[0], mainStr[1])
        if mulresult[0] == '-':
            isMinus = not isMinus
            mulresult = mulresult[1:]
        mainStr = mulresult + mainStr[2:]

    if mainStr == "k" and not isMinus :
        print("YES")
    else :
        print("NO")

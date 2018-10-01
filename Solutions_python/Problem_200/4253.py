def holds_condition(nArr):
    for i in range(0, len(nArr) - 1):
        temp_cur = int(nArr[i])
        temp_next = int(nArr[i+1])
        if temp_cur > temp_next:
            return False

    return True

def iterate(nArr):
    for i in range(0, len(nArr) - 1):
        temp_cur = int(nArr[i])
        temp_next = int(nArr[i+1])
        if temp_cur > temp_next:
            nArr[i] = str(temp_cur - 1)
            for j in range(i+1, len(nArr)):
                nArr[j] = "9"
            break

def lastTidyNumber(n):
    strN = str(n)
    nArr = []

    for i in range(0, len(strN)):
        nArr.append(strN[i])

    while not holds_condition(nArr):
        iterate(nArr)

    lastTidy = ""
    for memb in nArr:
        lastTidy = lastTidy + memb

    return lastTidy


def main():
    #t = int(raw_input())
    f = open("B-large.in", 'r')
    out = open("output.txt", 'w')
    t = int(f.readline())
    resInts = []
    for i in range(0, t):
        n = int(f.readline())
        resStr = lastTidyNumber(n)
        resInt = int(resStr)
        resInts.append(resInt)

    for i in range(0, t):
        res = "Case #" + str(i+1) + ": " + str(resInts[i]) + "\n"
        out.write(res)

main()

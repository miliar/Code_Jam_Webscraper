def howManyFlips(s, k):
    i = 0
    flips = 0
    foundMinus = False
    while i + k <= len(s):
        foundMinus = False
        if s[i] == "-":
            flips += 1
            newI = i
            for j in range(k):
                if s[i + j] == "+":
                    s[i + j] = "-"
                    if foundMinus == False:
                        newI = i + j
                        foundMinus = True
                else:
                    s[i + j] = "+"
            if foundMinus == False:
                newI = i + j + 1
            i = newI
        else:
            i += 1
    if foundMinus:
        return "Impossible"
    index = len(s) - k
    while index < len(s):
        if s[index] != "+":
            return "Impossible"
        index += 1
    return flips


N = int(input())
for i in range(N):
    s = input()
    l, k = s.split(" ")
    l = list(l)
    k = int(k)
    print("Case #{}: {}".format(i + 1, howManyFlips(l, k)))

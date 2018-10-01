def solve(k):
    while True:
        D = [int(d) for d in k]
        i = None
        for i in range(1, len(D)):
            if D[i - 1] > D[i]: break

        if i is None or D[i - 1] <= D[i]: return k

        k = str(int("".join(str(D[j]) for j in range(i - 1)) + str(D[i - 1] - 1) + "".join("9" for j in range(i, len(D)))))


def input(file):
    F = open(file, "r")
    T = int(F.readline())
    for i in range(T):
        yield i + 1, F.readline().strip()

out = open("S.out", "w")

#for (i, k) in input("Bsample.in"):
#for (i, k) in input("B-small-attempt0.in"):
for (i, k) in input("B-large.in"):
    #print("Case #%d: %s" % (i, solve(k)))
    print("Case #%d: %s" % (i, solve(k)), file = out)

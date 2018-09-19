__author__ = 'Lucas'


def war(N, naomi, ken):
    print(naomi)
    print(ken)
    winCount = 0
    naomiCount = 0
    for i in range(N):
        if naomi[naomiCount] > ken[i]:
            winCount += 1
        else:
            if naomiCount >= N:
                break
            else:
                naomiCount += 1
    return winCount


def deceit(N, naomi, ken):
    wincount = 0
    kencount = 0
    for i in range(N):
        if naomi[i] < ken[kencount]:
            continue
        else:
            wincount += 1
            kencount += 1
    return wincount


def testCase(N, naomi, ken, w, num):
    warresult = war(N, naomi, ken)
    deceitresult = deceit(N, naomi, ken)
    w.write("Case #" + str(num) + ": " + str(deceitresult) + " " + str(warresult))
    w.write("\n")


def main():
    f = open('input.in', 'r')
    w = open('output.out', 'w')

    T = int(f.readline().split()[0])
    for t in range(T):
        N = int(f.readline().split()[0])
        naomi = list(map(float, f.readline().split()))
        ken = list(map(float, f.readline().split()))
        naomi.sort()
        ken.sort()
        testCase(N, naomi, ken, w, t+1)



if __name__ == "__main__": main()
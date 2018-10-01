# RPI Google Code Jam
# zbanks Zach Banks zach@zbanks.net
# Python


def main():
    f = open("input.txt")
    testlen = int(f.readline().strip())
    tests = []
    
    for t in range(testlen):
        n = int(f.readline().strip())
        tests.append([])
        for i in range(n):
            tests[-1].append(list(f.readline().strip()))

    tests = tests[:testlen]

    for test, i in zip(tests, range(testlen)):
        print "Case #%d:\n%s" % (i+1, solve(test))

def parse(test):
    test = test.split(" ")
    return zip(test[1::2], map(int, test[2::2]))

def solve(test):
    nteams = len(test)
    ngames = map(lambda x: nteams - x.count("."), test)
    wp = map(lambda x: x.count("1") / float(nteams - x.count(".")), test)
    owps = [0.0] * nteams
    owp = [0.0] * nteams
    oowps = [0.0] * nteams
    oowp = [0.0] * nteams
   

    for i in range(nteams):
        row = test[i]
        nt = float(ngames[i] - 1)
        wins = row.count("1")
        for j in range(nteams):
            if row[j] == "1":
                owps[j] += (wins - 1) / nt
            elif row[j] == "0":
                owps[j] += wins / nt
    
    owp = map(lambda x: x[0] / float(x[1]), zip(owps, ngames))
    
    for i in range(nteams):
        row = test[i]
        for j in range(nteams):
            if row[j] != ".":
                oowps[j] += owp[i]
    
    oowp = map(lambda x: x[0] / float(x[1]), zip(oowps, ngames))
    rpi = map(lambda x: x[0] * 0.25 + x[1] * 0.5 + x[2] * 0.25, zip(wp, owp, oowp))

    return "\n".join(map(str, rpi))

if __name__ == "__main__":
    main()
